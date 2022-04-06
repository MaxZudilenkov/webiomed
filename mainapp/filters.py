import django_filters

from mainapp.models import TreatmentCase


class TreatmentCaseFilter(django_filters.FilterSet):
    class Meta:
        model = TreatmentCase
        fields = ['patient']


