from django.shortcuts import render, redirect
from django.views.generic import ListView

from mainapp.forms import AddPatientForm
from mainapp.models import Patient, TreatmentCase


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


def add_patient(request):
    if request.method == 'POST':
        form = AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list_view')
    form = AddPatientForm()
    context = {'form': form}
    return render(request, 'mainapp/add_patient.html', context)


class TreatmentCaseListView(ListView):
    template_name = 'mainapp/cases_list.html'
    context_object_name = 'cases'

    def get_queryset(self):
        return TreatmentCase.objects.all()
