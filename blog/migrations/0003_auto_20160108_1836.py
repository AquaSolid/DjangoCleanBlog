# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160108_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 18, 36, 56, 106913)),
        ),
    ]
