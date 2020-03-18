# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-18 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
