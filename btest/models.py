from django.db import models


class Mapclient(models.Model):
    familija = models.CharField(max_length=40, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    otchestvo = models.CharField(max_length=20, verbose_name='Отчество')
    nomer = models.CharField(max_length=10, verbose_name='Номер')
    strahovojpolis = models.CharField(max_length=16, verbose_name='Номер страхового полиса')
    datecreation = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Дата поступления')
    patientaddress = models.CharField(max_length=70, verbose_name='Адрес пациента')
    passportseries = models.CharField(max_length=4, verbose_name='Серия паспорта')
    passportid = models.CharField(max_length=6, verbose_name='Номер паспорта')
    

    class Meta:
        verbose_name_plural = 'Карты пациентов'
        verbose_name = 'Карта пациента'
        ordering = ['-datecreation']
        
class Bolnichnyepalaty(models.Model):
    jetazh = models.CharField(max_length=9, verbose_name='Этаж')
    nomer = models.CharField(max_length=3, verbose_name='Номер')
    vmeshhaemost = models.CharField(max_length=2, verbose_name='Вместимость')
    

    class Meta:
        verbose_name_plural = 'Больничные палаты'
        verbose_name = 'Больничная палата'
        ordering = ['-nomer']
        
class Spisokperiodov(models.Model):
    pacient = models.CharField(max_length=30, verbose_name='Пациент')
    datapostuplenija  = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Дата поступления')
    diagnoz = models.TextField(null=True, blank=True, verbose_name='Диагноз')
    datavypiski  = models.CharField(max_length=12,verbose_name='Дата выписки')
    palata = models.CharField(max_length=3, verbose_name='Палата')

    class Meta:
        verbose_name_plural = 'Амбулаторные периоды'
        verbose_name = 'Амбулаторный период'
        ordering = ['-datapostuplenija']