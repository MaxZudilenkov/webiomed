from django import forms

from mainapp.models import Patient


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('fullname', 'date_of_birth', 'sex')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1900, 2022), )
        }
