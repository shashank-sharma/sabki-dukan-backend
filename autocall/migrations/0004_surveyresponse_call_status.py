# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-17 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocall', '0003_auto_20190317_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='call_status',
            field=models.CharField(default='NOT', max_length=20),
        ),
    ]
