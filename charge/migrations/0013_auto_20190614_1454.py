# Generated by Django 2.0 on 2019-06-14 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0012_auto_20190610_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='payment',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(50)], verbose_name='Payment'),
        ),
    ]
