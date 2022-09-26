# Generated by Django 4.1.1 on 2022-09-26 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty_parlour', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'Мастер', 'verbose_name_plural': 'Мастера'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='master',
            name='experience',
            field=models.TextField(blank=True, null=True, verbose_name='Опыт'),
        ),
        migrations.AddField(
            model_name='master',
            name='information',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='master',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка для профиля'),
        ),
        migrations.AddField(
            model_name='master',
            name='position',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Позиция'),
        ),
        migrations.AddField(
            model_name='request',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Выбор даты'),
        ),
        migrations.AddField(
            model_name='request',
            name='master',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beauty_parlour.master', verbose_name='Запись к мастеру'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Имя для записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='phone',
            field=models.BigIntegerField(default=1, verbose_name='Номер телефона клиента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beauty_parlour.services'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='sms',
            field=models.TextField(blank=True, null=True, verbose_name='Поле для смс'),
        ),
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Выбор времени'),
        ),
        migrations.AddField(
            model_name='services',
            name='master',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beauty_parlour.master', verbose_name='Мастер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название услуг'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='master',
            table='masters',
        ),
        migrations.AlterModelTable(
            name='request',
            table='request',
        ),
        migrations.AlterModelTable(
            name='services',
            table='services',
        ),
    ]
