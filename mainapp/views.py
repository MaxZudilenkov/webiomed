from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView

from mainapp.filters import TreatmentCaseFilter
from mainapp.forms import AddPatientForm, AddTreatmentCaseForm
from mainapp.models import Patient, TreatmentCase, MedicalDocument


class PatientListView(ListView):
    # Класс для отображения списка пациентов
    template_name = 'mainapp/patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.all()


class PatientDetailView(ListView):
    # Класс для отображения конкртеного пацииента
    model = Patient
    template_name = 'mainapp/patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['pk'])
        return context


def add_patient(request):
    # Метод для добавления пацииента
    if request.method == 'POST':
        form = AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list_view')
    form = AddPatientForm()
    context = {'form': form}
    return render(request, 'mainapp/add_patient.html', context)


def add_case(request):
    # Класс для добавления случая лечения
    if request.method == 'POST':
        form = AddTreatmentCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list_view')
    form = AddTreatmentCaseForm()
    context = {'form': form}
    return render(request, 'mainapp/add_case.html', context)


class TreatmentCaseListView(ListView):
    # Класс для отображения списка случаев лечения
    template_name = 'mainapp/cases_list.html'
    context_object_name = 'cases'

    def get_queryset(self):
        return TreatmentCase.objects.all()

    def get_context_data(self, **kwargs):
        my_filter = TreatmentCaseFilter(self.request.GET, queryset=TreatmentCase.objects.all())
        context = super().get_context_data(**kwargs)
        context['my_filter'] = my_filter
        context['cases'] = my_filter.qs
        return context


class TreatmentCaseDetailView(ListView):
    # Класс для отображения конкретного случая лечения
    model = Patient
    template_name = 'mainapp/case_detail.html'

    def get_context_data(self, **kwargs):
        current_case = int(self.request.get_full_path().split('/')[2])
        print(current_case)
        context = super().get_context_data(**kwargs)
        context['documents'] = MedicalDocument.objects.filter(case=current_case)
        return context
