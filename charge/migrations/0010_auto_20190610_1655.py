# Generated by Django 2.0 on 2019-06-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0009_charge_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
    ]
