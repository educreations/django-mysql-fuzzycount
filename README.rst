Django MySQL Fuzzycount
=======================

When using MySQL, `counting all rows`_ is very expensive on large InnoDB tables. This is a replacement for ``QuerySet`` that returns an approximation if ``COUNT(*)`` is called with no additional constraints. In all other cases it should behave exactly as QuerySet.

This only works with MySQL and behaves normally for all other engines.


.. _`counting all rows`: http://www.mysqlperformanceblog.com/2006/12/01/count-for-innodb-tables/
