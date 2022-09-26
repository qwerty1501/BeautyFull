from datetime import timedelta
from django.utils import timezone

from django.db import models


class Master(models.Model):

    """ Модель мастеров """

    name = models.CharField(
        max_length=250, null=True, blank=False, verbose_name='Имя'
    )
    picture = models.ImageField(
        null=True, blank=True, verbose_name='Картинка для профиля'
    )
    information = models.TextField(
        verbose_name='Информация', null=True, blank=True
    )
    experience = models.TextField(
        verbose_name='Опыт', null=True, blank=True
    )
    position = models.CharField(
        max_length=250, verbose_name='Позиция', null=True, blank=True
    )


    class Meta:
        db_table = 'masters'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
        
    def __str__(self):
        return self.name
    


class Services(models.Model):

    """ Модель для услуг """

    title = models.CharField(
        max_length=255, verbose_name='Название услуг'
    )
    master = models.ForeignKey(
        to=Master, on_delete=models.CASCADE, verbose_name='Мастер'
    )


    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"
        
    def __str__(self):
        return self.title
    


class Request(models.Model):

    """ Модель для Записи """

    master = models.ForeignKey(
        to=Master, on_delete=models.CASCADE, verbose_name='Запись к мастеру',
    )
    time = models.TimeField(
        verbose_name='Выбор времени', auto_now_add=True, blank=True, null=True
    )
    date = models.DateField(
        verbose_name='Выбор даты', auto_now_add=True, blank=True, null=True
    )
    service = models.ForeignKey(
        to=Services, on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255, verbose_name='Имя для записи'
    )
    phone = models.BigIntegerField(
        verbose_name='Номер телефона клиента'
    )
    sms = models.TextField(
        null=True, blank=True, verbose_name='Поле для смс'
    )


    class Meta:
        db_table = 'request'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.name