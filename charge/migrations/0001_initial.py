# Generated by Django 2.0 on 2019-06-29 21:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=20, verbose_name='Description')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10, verbose_name='Status')),
                ('payment', models.IntegerField(validators=[django.core.validators.MinValueValidator(6000), django.core.validators.MaxValueValidator(50000)], verbose_name='Payment')),
            ],
            options={
                'verbose_name': 'Charge',
                'verbose_name_plural': 'Charges',
            },
        ),
        migrations.CreateModel(
            name='ChargeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateField(verbose_name='Initial date')),
                ('final_date', models.DateField(verbose_name='Final date')),
                ('motive_movement', models.CharField(max_length=300, verbose_name='Motive of movement')),
                ('authorized_for', models.CharField(max_length=20, verbose_name='Authorized for')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10, verbose_name='Status')),
                ('charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Charge', verbose_name='Charge')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Historial de cargo',
                'verbose_name_plural': 'Historial de cargos',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.AddField(
            model_name='charge',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Department', verbose_name='Department'),
        ),
    ]