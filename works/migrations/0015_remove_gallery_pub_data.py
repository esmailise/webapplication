# Generated by Django 3.1.7 on 2021-03-29 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0014_auto_20210329_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='pub_data',
        ),
    ]