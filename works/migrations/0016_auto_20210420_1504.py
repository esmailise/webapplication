# Generated by Django 3.1.7 on 2021-04-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0015_remove_gallery_pub_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'گالری', 'verbose_name_plural': 'گالری ها'},
        ),
        migrations.AlterModelOptions(
            name='works',
            options={'verbose_name': 'کار', 'verbose_name_plural': 'کار ها'},
        ),
    ]