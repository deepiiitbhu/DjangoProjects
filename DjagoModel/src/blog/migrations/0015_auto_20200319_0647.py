# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-19 06:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200319_0641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='ctime',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='uptime',
            new_name='updated',
        ),
    ]