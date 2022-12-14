# Generated by Django 4.1.1 on 2022-09-29 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "beauty_parlour",
            "0003_remove_master_experience_remove_master_information_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="services",
            name="master",
        ),
        migrations.AddField(
            model_name="master",
            name="service",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="beauty_parlour.services",
                verbose_name="Название вашу услугу",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="master",
            name="experience_en",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Опишите свой опыт работы на Англиском",
            ),
        ),
        migrations.AlterField(
            model_name="master",
            name="experience_ky",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Опишите свой опыт работы на Кыргызском",
            ),
        ),
        migrations.AlterField(
            model_name="master",
            name="experience_ru",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Опишите свой опыт работы на Русском",
            ),
        ),
        migrations.AlterField(
            model_name="master",
            name="information_en",
            field=models.TextField(
                blank=True, null=True, verbose_name="Автобиография на Англиском"
            ),
        ),
        migrations.AlterField(
            model_name="master",
            name="information_ky",
            field=models.TextField(
                blank=True, null=True, verbose_name="Автобиография на Кыргызском"
            ),
        ),
        migrations.AlterField(
            model_name="master",
            name="information_ru",
            field=models.TextField(
                blank=True, null=True, verbose_name="Автобиография на Русском"
            ),
        ),
    ]
