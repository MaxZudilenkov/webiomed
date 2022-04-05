from django.urls import path

from mainapp.views import PatientListView, PatientDetailView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name="patient_list_view"),
    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient_detail"),

]
