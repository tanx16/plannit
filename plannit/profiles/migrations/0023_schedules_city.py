# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('profiles', '0022_remove_schedules_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='city_schedules', to='cities_light.City'),
        ),
    ]
