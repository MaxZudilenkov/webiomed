from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Patient


class PatientListView(ListView):
    template_name = 'mainapp/patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.all()


class PatientDetailView(ListView):
    model = Patient
    template_name = 'mainapp/patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['pk'])
        return context
