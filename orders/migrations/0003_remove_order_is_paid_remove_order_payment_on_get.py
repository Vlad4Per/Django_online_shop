# Generated by Django 4.2.17 on 2025-01-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_address_order_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_on_get',
        ),
    ]
