# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptest', '0003_auto_20160427_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
