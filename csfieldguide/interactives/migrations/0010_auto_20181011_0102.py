# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-11 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactives', '0009_auto_20180912_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactive',
            name='name_de',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='interactive',
            name='template_de',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
