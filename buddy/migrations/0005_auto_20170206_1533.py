# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-06 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0004_auto_20170206_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddydetail',
            name='batch_time',
            field=models.TimeField(blank=True, help_text='Time format is :HH:MM:SS', null=True),
        ),
    ]