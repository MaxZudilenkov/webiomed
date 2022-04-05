from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Patient


class PatientView(ListView):
    template_name = 'mainapp/patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.all()
