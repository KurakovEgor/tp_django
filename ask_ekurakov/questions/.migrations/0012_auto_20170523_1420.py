# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 11:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20170523_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 23, 11, 20, 48, 50478, tzinfo=utc), verbose_name='Дата Добавления'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 5, 23, 11, 20, 48, 51818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='register_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 23, 11, 20, 48, 49348, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
    ]
