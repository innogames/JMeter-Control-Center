# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 14:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0004_auto_20170323_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='jmeter_destination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='jmeter_parameters',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='jvm_args',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='test_plan_destination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
