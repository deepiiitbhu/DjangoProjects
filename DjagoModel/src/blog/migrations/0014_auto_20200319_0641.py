# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-19 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200319_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='timestamp',
            new_name='ctime',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='timezone',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='uptime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
