# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-04 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buggy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='time_type',
            field=models.CharField(default=datetime.datetime(2018, 6, 4, 18, 30, 43, 788341, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]