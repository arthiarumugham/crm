# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Moderate'), ('L', 'Low')], default='L', max_length=10)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('raised_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]