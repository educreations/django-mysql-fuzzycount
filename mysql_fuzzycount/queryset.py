import logging

from django.conf import settings
from django.db import connections
from django.db.models.query import QuerySet

log = logging.getLogger(__name__)


class FuzzyCountQuerySet(QuerySet):
    """Counting all rows is very expensive on large InnoDB tables. This
    is a replacement for QuerySet that returns an approximation if count()
    is called with no additional constraints. In all other cases it should
    behave exactly as QuerySet.

    Only works with MySQL. Behaves normally for all other engines.
    """

    def count(self):
        """Override QuerySet.count to approximate count in some situations."""

        # If there are results already, return the result cache count
        if self._result_cache is not None and not self._iter:
            return len(self._result_cache)

        mysql_engines = ("mysql", )
        engine = settings.DATABASES[self.db]["ENGINE"].split(".")[-1]
        is_mysql = engine.startswith(mysql_engines)

        query = self.query

        is_filtered = (query.where
                       or query.high_mark
                       or query.low_mark
                       or query.select
                       or query.group_by
                       or query.having
                       or query.distinct)

        if not is_mysql or is_filtered:
            # We do not have a MySQL database or there are constraints on the
            # query. Let Django's default handle this.
            return super(FuzzyCountQuerySet, self).count()

        # The query has no constraints, so we would be doing a select COUNT(*)
        # across the entire table. Query the table status to get an
        # approximation instead.
        cursor = connections[self.db].cursor()
        cursor.execute(
            "SHOW TABLE STATUS LIKE %s;", (self.model._meta.db_table, ))
        return int(cursor.fetchall()[0][4])
