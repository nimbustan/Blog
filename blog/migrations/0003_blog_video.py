# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, default='Videos/love.mp4', upload_to='Videos/%Y/%m/%d'),
        ),
    ]
