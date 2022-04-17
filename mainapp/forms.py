from django import forms

from mainapp.models import Patient, TreatmentCase, MedicalDocument, DocumentBody


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


class AddMedicalDocumentForm(forms.ModelForm):
    # Форма для добавления документа
    class Meta:
        model = MedicalDocument
        fields = ('patient', 'case', 'title',)


class AddDocumentBodyForm(forms.ModelForm):
    # Форма для добавления тела документа
    class Meta:
        model = DocumentBody
        fields = ('filling',)

class RequestTimeForm(forms.Form):
    request_time = forms.IntegerField(min_value=1, max_value=9999)