# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-31 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0007_auto_20181228_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='selection',
            field=models.CharField(default='M', max_length=1),
        ),
    ]