from model_utils.managers import PassThroughManager

from mysql_fuzzycount.queryset import FuzzyCountQuerySet


FuzzyCountManager = PassThroughManager.for_queryset_class(FuzzyCountQuerySet)
