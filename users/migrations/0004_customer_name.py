# Generated by Django 3.1.7 on 2021-08-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210808_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='نام کاربری'),
        ),
    ]
