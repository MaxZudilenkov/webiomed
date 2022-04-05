from django.db import models


class Patient(models.Model):
    # Класс пациента
    CHOICES = [
        (1, ' Мужской'),
        (2, ' Женский')
    ]
    fullname = models.CharField(max_length=200, verbose_name="ФИО")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    sex = models.PositiveSmallIntegerField(verbose_name="Пол", choices=CHOICES)


class TreatmentCase(models.Model):
    # Класс случая лечения
    CHOICES = [
        (1, ' Положительный'),
        (2, ' Отрицательный')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="case")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания", null=True)
    result = models.PositiveSmallIntegerField(verbose_name="Исход", choices=CHOICES, null=True)


class MedicalDocument(models.Model):
    # Класс медицинского документа
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="document_patient")
    case = models.ForeignKey(TreatmentCase, on_delete=models.CASCADE, related_name="document_case", null=True)
    title = models.CharField(verbose_name="Заголовок")
    document_date = models.DateField(verbose_name="Дата документа")


class DocumentBody(models.Model):
    # Класс тела документа
    document = models.OneToOneField(MedicalDocument, verbose_name="Привязка к документу", on_delete=models.CASCADE)
    filling = models.JSONField(verbose_name="Наполнение документа")


class RequestLog(models.Model):
    # Класс лога запросов
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время логгирования")
    request_filling = models.JSONField(verbose_name="Наполнение ответа")
