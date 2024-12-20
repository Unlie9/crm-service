# Generated by Django 5.1.3 on 2024-11-16 15:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('note', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('inv_amount', models.IntegerField(blank=True, help_text='Сумма за услуги компании', null=True)),
                ('ord', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True)),
            ],
        ),
    ]
