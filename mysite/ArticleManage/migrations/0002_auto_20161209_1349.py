# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 05:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArticleManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=500)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 12, 9, 5, 49, 39, 38063, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='column',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_column', to='ArticleManage.ArticleColumn'),
        ),
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together=set([('id', 'slug')]),
        ),
    ]