# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metodo', '0003_auto_20180720_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='causa',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
