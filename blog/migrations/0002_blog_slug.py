# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, help_text='Link otomatik alinir, Lutfen Degistirmeyiniz!', max_length=80, null=True),
        ),
    ]
