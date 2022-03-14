# Generated by Django 3.1.7 on 2021-08-08 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0017_auto_20210805_1355'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0007_auto_20210808_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(choices=[(False, 'انجام نشده'), (True, 'انجام شده')], default=True, null=True, verbose_name='وضعیت کار'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='categorys',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.category', verbose_name='نوع کار'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربر'),
        ),
    ]