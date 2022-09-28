from datetime import timedelta
from django.utils import timezone

from django.db import models


class Master(models.Model):

    """ Модель мастеров """

    name_ky = models.CharField(
        max_length=250, null=True, blank=False, verbose_name='Ведите имя на Кыргызском'
    )
    name_en = models.CharField(
        max_length=250, blank=True, null=True, verbose_name='Ведите имя на Англиском'
    )
    name_ru = models.CharField(
        max_length=250, blank=True, null=True, verbose_name='Ведите имя на Русском'
    )
    picture = models.ImageField(
        null=True, blank=True, verbose_name='Картинка для профиля'
    )
    information_ky = models.TextField(
        verbose_name='Информация на Кыргызском', null=True, blank=True
    )
    information_en = models.TextField(
        verbose_name='Информация на Англиском', null=True, blank=True
    )
    information_ru = models.TextField(
        verbose_name='Информация на Русском', null=True, blank=True
    )
    experience_ky = models.TextField(
        verbose_name='Опишите свой опыт работы на Кыргызском', null=True, blank=True
    )
    experience_en = models.TextField(
        verbose_name='Опишите свой опыт работы на Англиском', null=True, blank=True
    )
    experience_ru = models.TextField(
        verbose_name='Опишите свой опыт работы на Русском', null=True, blank=True
    )
    position_ky = models.CharField(
        max_length=250, verbose_name='Позиция на Кыргызском', null=True, blank=True
    )
    position_en = models.CharField(
        max_length=250, verbose_name='Позиция на Англизском', null=True, blank=True
    )
    position_ru = models.CharField(
        max_length=250, verbose_name='Позиция на Русском', null=True, blank=True
    )


    class Meta:
        db_table = 'masters'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
        
    def __str__(self):
        return self.name_ru
    


class Services(models.Model):

    """ Модель для услуг """

    title_ky = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Название услуг на Кыргызском'
    )
    title_en = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Название услуг на Англиском'
    )
    title_ru = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Название услуг на Русском'
    )
    master = models.ForeignKey(
        to=Master, on_delete=models.CASCADE, verbose_name='Мастер'
    )


    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"
        
    def __str__(self):
        return self.title_ru
    


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