from django.contrib import admin
from django.template.defaultfilters import truncatechars

from mainapp.models import Patient, TreatmentCase, MedicalDocument, DocumentBody, RequestLog


class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.fields]


class TreatmentCaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TreatmentCase._meta.fields]


class MedicalDocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MedicalDocument._meta.fields]


class DocumentBodyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DocumentBody._meta.fields]


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp']


admin.site.register(Patient, PatientAdmin)
admin.site.register(TreatmentCase, TreatmentCaseAdmin)
admin.site.register(MedicalDocument, MedicalDocumentAdmin)
admin.site.register(DocumentBody, DocumentBodyAdmin)
admin.site.register(RequestLog, RequestLogAdmin)
