# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20171007_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedules',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='events',
            name='schedule',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='profiles.schedules'),
            preserve_default=False,
        ),
    ]
