from django.urls import path

from mainapp.views import PatientListView, PatientDetailView, add_patient, TreatmentCaseListView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name="patient_list_view"),
    path('cases/', TreatmentCaseListView.as_view(), name="patient_list_view"),
    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient_detail"),
    path('add_patient/', add_patient, name="patient_detail"),
]
