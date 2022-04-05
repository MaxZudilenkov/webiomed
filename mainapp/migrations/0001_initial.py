# Generated by Django 4.0.3 on 2022-04-05 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.PositiveSmallIntegerField(choices=[(1, ' Мужской'), (2, ' Женский')], verbose_name='Пол')),
            ],
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время логгирования')),
                ('request_filling', models.JSONField(verbose_name='Наполнение ответа')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('result', models.PositiveSmallIntegerField(blank=True, choices=[(1, ' Положительный'), (2, ' Отрицательный')], null=True, verbose_name='Исход')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='mainapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('document_date', models.DateField(verbose_name='Дата документа')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_case', to='mainapp.treatmentcase')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_patient', to='mainapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling', models.JSONField(verbose_name='Наполнение документа')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.medicaldocument', verbose_name='Привязка к документу')),
            ],
        ),
    ]
