# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(),
        ),
    ]
