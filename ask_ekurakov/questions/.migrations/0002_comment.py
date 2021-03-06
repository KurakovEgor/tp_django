# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Решение')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Article')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
