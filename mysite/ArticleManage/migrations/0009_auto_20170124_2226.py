# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-24 14:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleManage', '0008_auto_20170124_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 24, 14, 26, 34, 860276, tzinfo=utc)),
        ),
    ]