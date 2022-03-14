# Generated by Django 3.1.7 on 2021-08-05 09:25

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkAcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام رسانه')),
                ('Acounturl', models.URLField(verbose_name='ادرس رسانه')),
                ('icons', models.CharField(choices=[('fa fa-facebook', 'فیس بوک'), ('fa fa-twitter', 'توییتر'), ('fa fa-linkedin', 'لینک دین'), ('fa fa-google-plus', 'گوگل پلاس'), ('fa fa-instagram', 'اینستا گرام'), ('fa fa-telegram', 'تلگرام'), ('fa fa-whatsapp', 'واتس اپ')], max_length=200, verbose_name='انتخاب شمایل')),
            ],
            options={
                'verbose_name': 'رسانه  اجتماعی',
                'verbose_name_plural': 'رسانه های اجتماعی',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('summary', models.TextField(verbose_name='خلاصه درباره ما')),
                ('content', ckeditor.fields.RichTextField(verbose_name='محتوا درباره')),
                ('photo', models.ImageField(upload_to='aboutus/', verbose_name='عکس')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('links', models.ManyToManyField(to='aboutus.LinkAcount', verbose_name='رسانه ها')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]
