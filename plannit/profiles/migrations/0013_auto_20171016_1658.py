# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20171016_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_schedules', to='profiles.city'),
        ),
    ]
