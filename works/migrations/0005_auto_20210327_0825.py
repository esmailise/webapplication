# Generated by Django 3.1.7 on 2021-03-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20210326_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='work',
            field=models.CharField(choices=[('B', 'بازدید کار'), ('P', 'پمپ آب'), ('M', 'موتور خانه')], default='P', max_length=50, verbose_name='کار'),
        ),
    ]
