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


class Services(models.Model):

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


class Request(models.Model):

    master = models.ForeignKey(

    )