# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-29 01:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20170428_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 29, 1, 0, 53, 232126, tzinfo=utc)),
        ),
    ]