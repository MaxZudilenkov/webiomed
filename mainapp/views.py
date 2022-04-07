import form as form
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from mainapp.filters import TreatmentCaseFilter, MedicalDocumentFilter
from mainapp.forms import AddPatientForm, AddTreatmentCaseForm, AddMedicalDocumentForm, AddDocumentBodyForm
from mainapp.models import Patient, TreatmentCase, MedicalDocument, DocumentBody


class PatientListView(ListView):
    # Класс для отображения списка пациентов
    template_name = 'mainapp/patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.all()


class PatientDetailView(DetailView):
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


def add_document(request):
    # Класс для добавления документа и тела документа
    if request.method == 'POST':
        document_form = AddMedicalDocumentForm(request.POST)
        body_form = AddDocumentBodyForm(request.POST)
        filling = request.POST.get('filling')
        if document_form.is_valid():
            model_instance = document_form.save(commit=False)
            mn_instance = model_instance
            mn_instance.save()
            DocumentBody.objects.create(document=MedicalDocument.objects.last(), filling=filling)
    else:
        document_form = AddMedicalDocumentForm()
        body_form = AddDocumentBodyForm()
    context = {'document_form': document_form, 'body_form': body_form}
    return render(request, 'mainapp/add_document.html', context)


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
        context = super().get_context_data(**kwargs)
        context['documents'] = MedicalDocument.objects.filter(case=current_case)
        return context


class MedicalDocumentListView(ListView):
    # Класс для отображения списка документов
    template_name = 'mainapp/documents_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        return MedicalDocument.objects.all()

    def get_context_data(self, **kwargs):
        my_filter_patient = TreatmentCaseFilter(self.request.GET, queryset=MedicalDocument.objects.all())
        my_filter_case = MedicalDocumentFilter(self.request.GET, queryset=MedicalDocument.objects.all())
        context = super().get_context_data(**kwargs)
        context['my_filter_patient'] = my_filter_patient
        context['my_filter_case'] = my_filter_case
        if 'filter_by_case' in self.request.GET:
            context['documents'] = my_filter_case.qs
        if 'filter_by_patient' in self.request.GET:
            context['documents'] = my_filter_patient.qs
        return context


class DocumentDetailView(ListView):
    # Класс для отображения конкретного документа
    model = DocumentBody
    template_name = 'mainapp/document_detail.html'

    def get_context_data(self, **kwargs):
        current_document = int(self.request.get_full_path().split('/')[2])
        print(current_document)
        context = super().get_context_data(**kwargs)
        try:
            DocumentBody.objects.get(document=current_document)
            context['bodies'] = DocumentBody.objects.get(document=current_document)
        except DocumentBody.DoesNotExist:
            context['bodies'] = ''
        return context
