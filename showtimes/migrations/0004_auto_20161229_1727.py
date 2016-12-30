# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0003_showtime_last_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='cinema',
            field=models.CharField(choices=[('CIVIL', 'QFX Civil Mall'), ('LABIM', 'QFX LABIM Mall'), ('KUMARI', 'QFX Kumari'), ('JAINEPAL', 'QFX Jai Nepal')], max_length=10),
        ),
    ]