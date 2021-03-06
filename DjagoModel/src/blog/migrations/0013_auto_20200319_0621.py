# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-19 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200319_0604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={},
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='publish_datw',
            new_name='publish_date',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='timezone',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
