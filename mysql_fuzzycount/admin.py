from django.contrib import admin

from mysql_fuzzycount.queryset import FuzzyCountQuerySet


class FuzzyCountModelAdminMixin(object):

    def queryset(self, request):
        qs = super(FuzzyCountModelAdminMixin, self).queryset(request)
        return qs._clone(klass=FuzzyCountQuerySet)


class FuzzyCountModelAdmin(FuzzyCountModelAdminMixin, admin.ModelAdmin):
    pass
