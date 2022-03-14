# Generated by Django 3.1.7 on 2021-08-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_customer_work'),
        ('reservation', '0004_remove_reservation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]