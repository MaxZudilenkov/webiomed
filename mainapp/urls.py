from django.urls import path

from mainapp.views import PatientListView, PatientDetailView, add_patient, TreatmentCaseListView, \
    TreatmentCaseDetailView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name="patient_list_view"),
    path('cases/', TreatmentCaseListView.as_view(), name="case_list_view"),
    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient_detail"),
    path('case/<int:pk>', TreatmentCaseDetailView.as_view(), name="case_detail"),
    path('add_patient/', add_patient, name="patient_detail"),
]
