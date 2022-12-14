# Generated by Django 4.1.1 on 2022-09-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beauty_parlour", "0002_alter_master_options_alter_request_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="master",
            name="experience",
        ),
        migrations.RemoveField(
            model_name="master",
            name="information",
        ),
        migrations.RemoveField(
            model_name="master",
            name="name",
        ),
        migrations.RemoveField(
            model_name="master",
            name="position",
        ),
        migrations.RemoveField(
            model_name="services",
            name="title",
        ),
        migrations.AddField(
            model_name="master",
            name="experience_en",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Опишите свой опыт работы на Англиском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="experience_ky",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Опишите свой опыт работы на Кыргызском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="experience_ru",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Опишите свой опыт работы на Русском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="information_en",
            field=models.TextField(
                blank=True, null=True, verbose_name="Информация на Англиском"
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="information_ky",
            field=models.TextField(
                blank=True, null=True, verbose_name="Информация на Кыргызском"
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="information_ru",
            field=models.TextField(
                blank=True, null=True, verbose_name="Информация на Русском"
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="name_en",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Ведите имя на Англиском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="name_ky",
            field=models.CharField(
                max_length=250, null=True, verbose_name="Ведите имя на Кыргызском"
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="name_ru",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Ведите имя на Русском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="position_en",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Позиция на Англизском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="position_ky",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Позиция на Кыргызском",
            ),
        ),
        migrations.AddField(
            model_name="master",
            name="position_ru",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Позиция на Русском"
            ),
        ),
        migrations.AddField(
            model_name="services",
            name="title_en",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Название услуг на Англиском",
            ),
        ),
        migrations.AddField(
            model_name="services",
            name="title_ky",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Название услуг на Кыргызском",
            ),
        ),
        migrations.AddField(
            model_name="services",
            name="title_ru",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Название услуг на Русском",
            ),
        ),
    ]
