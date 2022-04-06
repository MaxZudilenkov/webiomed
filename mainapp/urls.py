from django.urls import path

from mainapp.views import PatientListView, PatientDetailView, add_patient, TreatmentCaseListView, \
    TreatmentCaseDetailView, add_case, MedicalDocumentListView, MedicalDocumentDetailView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name="patient_list_view"),
    path('cases/', TreatmentCaseListView.as_view(), name="case_list_view"),
    path('documents/', MedicalDocumentListView.as_view(), name="document_list_view"),
    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient_detail"),
    path('case/<int:pk>', TreatmentCaseDetailView.as_view(), name="case_detail"),
    path('document/<int:pk>', MedicalDocumentDetailView.as_view(), name="document_detail"),
    path('add_patient/', add_patient, name="add_patient"),
    path('add_case/', add_case, name="add_case"),
]
