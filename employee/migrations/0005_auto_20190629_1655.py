# Generated by Django 2.0 on 2019-06-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20190629_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicstudies',
            name='institute',
            field=models.CharField(max_length=30, verbose_name='Institute'),
        ),
    ]