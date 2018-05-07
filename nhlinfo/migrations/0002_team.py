# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nhlinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=25)),
                ('team_abv', models.CharField(max_length=3)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='nhlinfo.Division')),
            ],
            options={
                'ordering': ['team_name', 'team_abv'],
            },
        ),
    ]
