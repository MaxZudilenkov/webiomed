from django.urls import path

from mainapp.views import PatientListView, PatientDetailView, add_patient, TreatmentCaseListView, \
    TreatmentCaseDetailView, add_case, MedicalDocumentListView, DocumentDetailView, add_document, \
    get_json_from_aiohttp_server

urlpatterns = [
    path('', PatientListView.as_view(), name="patient_list_view"),
    path('cases/', TreatmentCaseListView.as_view(), name="case_list_view"),
    path('documents/', MedicalDocumentListView.as_view(), name="document_list_view"),
    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient_detail"),
    path('case/<int:pk>', TreatmentCaseDetailView.as_view(), name="case_detail"),
    path('document/<int:pk>', DocumentDetailView.as_view(), name="document_detail"),
    path('add_patient/', add_patient, name="add_patient"),
    path('add_case/', add_case, name="add_case"),
    path('add_document/', add_document, name="add_document"),
    path('request_aiohttp/', get_json_from_aiohttp_server, name="get_json_from_aiohttp_server"),
]
