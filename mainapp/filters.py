import django_filters

from mainapp.models import TreatmentCase, MedicalDocument


class TreatmentCaseFilter(django_filters.FilterSet):
    class Meta:
        model = TreatmentCase
        fields = ['patient']

class MedicalDocumentFilter(django_filters.FilterSet):
    class Meta:
        model = MedicalDocument
        fields = ['case']
