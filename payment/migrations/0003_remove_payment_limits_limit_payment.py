# Generated by Django 5.1.3 on 2024-11-18 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_limit_remove_payment_limit_payment_limits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='limits',
        ),
        migrations.AddField(
            model_name='limit',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment'),
        ),
    ]
