# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-31 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_customer_selection'),
    ]

    operations = [
        migrations.CreateModel(
            name='serial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=-1, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.customer')),
            ],
        ),
    ]
