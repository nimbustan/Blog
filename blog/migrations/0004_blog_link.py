# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.URLField(default='https://www.youtube.com/embed/p4SPFiuL4CA'),
        ),
    ]