# Generated by Django 2.0 on 2019-06-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0007_auto_20190604_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='description',
            field=models.CharField(max_length=20, verbose_name='Description'),
        ),
    ]