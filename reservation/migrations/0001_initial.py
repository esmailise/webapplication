# Generated by Django 3.1.7 on 2021-08-05 09:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('works', '0017_auto_20210805_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u200cنام و خانوادگی')),
                ('email', models.EmailField(max_length=245, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('data', models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='ساعت')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('categorys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.category')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'رزرو ها',
            },
        ),
    ]
