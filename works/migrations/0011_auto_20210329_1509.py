# Generated by Django 3.1.7 on 2021-03-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0010_auto_20210329_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_work_en',
            field=models.CharField(max_length=50, verbose_name='نام کارانگلیسی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_work_fa',
            field=models.CharField(max_length=50, verbose_name='نام کار فارسی'),
        ),
    ]
