# Generated by Django 3.1.7 on 2021-08-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20210808_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(choices=[(False, 'انجام نشده'), (True, 'انجام شده')], default=False, null=True, verbose_name='وضعیت کار'),
        ),
    ]