# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-06 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhlinfo', '0009_defense_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forward',
            name='team',
        ),
        migrations.AlterField(
            model_name='forward',
            name='forward_ht',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='forward',
            name='forward_nat',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='forward',
            name='forward_pts',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='forward',
            name='forward_toi',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='forward',
            name='forward_wt',
            field=models.CharField(default=None, max_length=25),
        ),
    ]
