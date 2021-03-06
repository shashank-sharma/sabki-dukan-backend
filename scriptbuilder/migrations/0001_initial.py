# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-16 21:29
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptBuilder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('script_flow', django.contrib.postgres.fields.jsonb.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
