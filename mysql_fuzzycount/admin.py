from django.contrib import admin

from mysql_fuzzycount.queryset import FuzzyCountQuerySet


class FuzzyCountModelAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(FuzzyCountModelAdmin, self).queryset(request)
        return qs._clone(klass=FuzzyCountQuerySet)
