# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 11:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20170523_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 23, 11, 18, 26, 414484, tzinfo=utc), verbose_name='Дата Добавления'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 5, 23, 11, 18, 26, 415966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='register_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 23, 11, 18, 26, 413635, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
    ]
