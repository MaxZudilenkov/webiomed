from django.urls import path

from mainapp.views import PatientView

urlpatterns = [
    path('patients/', PatientView.as_view(), name="show_first_page"),

]
