from django import forms

from mainapp.models import Patient, TreatmentCase


class AddPatientForm(forms.ModelForm):
    # Форма для добавления пациента
    class Meta:
        model = Patient
        fields = ('fullname', 'date_of_birth', 'sex')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1900, 2022), )
        }


class AddTreatmentCaseForm(forms.ModelForm):
    # Форма для добавления случая лечения
    class Meta:
        model = TreatmentCase
        fields = ('patient', 'start_date', 'end_date', 'result')
        widgets = {
            'start_date': forms.SelectDateWidget(years=range(2010, 2022)),
            'end_date': forms.SelectDateWidget(years=range(2010, 2022)),
        }
