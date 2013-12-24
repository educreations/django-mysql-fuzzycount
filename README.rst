Django MySQL Fuzzycount
=======================

When using MySQL, `counting all rows`_ is very expensive on large InnoDB tables. This is a replacement for ``QuerySet`` that returns an approximation if ``COUNT(*)`` is called with no additional constraints. In all other cases it should behave exactly as QuerySet.

This only works with MySQL and behaves normally for all other engines.


Installation
------------

Install the package ``django-mysql-fuzzycount`` from PyPI using `pip`_::

    $ pip install -U django-mysql-fuzzycount


Usage
-----

There are a couple ways to use the ``FuzzyCountQuerySet``.

You can import and use the provided ``FuzzyCountManager`` on your Django models::

    from django.db import models

    from mysql_fuzzycount.managers import FuzzyCountManager

    class Choice(model.Model):
        objects = FuzzyCountManager()

        # ...

Then, doing a count on the ``Choice`` model, without any constraints, will approximate the total count::

    >>> Choice.objects.count()  # approximation
    100
    >>> Choice.objects.filter(votes__gt=10).count()  # not an approximation
    28

Another common issue is counts in the admin for a model. There is a base ``ModelAdmin`` class that you can subclass in your ``admin.py`` files to prevent expensive ``COUNT(*)`` queries upon loading the admin page. In an ``admin.py`` for one of your models::

    from django.contrib import admin

    from mysql_fuzzycount.admin import FuzzyCountModelAdmin

    from myapp.models import Choice


    class ChoiceAdmin(FuzzyCountModelAdmin):
        pass

    admin.site.register(Choice, ChoiceAdmin)

Now, when you load the admin page for the ``Choice`` model, the count for pagination will be approximate.


Testing
-------

It has been tested in production, but there are no unit or integration tests.


License
-------

Copyright © 2013, Educreations, Inc under the MIT LICENSE.


.. _`counting all rows`: http://www.mysqlperformanceblog.com/2006/12/01/count-for-innodb-tables/
.. _`pip`: http://www.pip-installer.org/
