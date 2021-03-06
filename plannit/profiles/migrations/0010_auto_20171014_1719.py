# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_schedules_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='person_likes',
            field=models.ManyToManyField(related_name='liked_schedules', to='profiles.person'),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_schedules', to='profiles.person'),
        ),
    ]
