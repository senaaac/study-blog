# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(to='feed.Hashtag'),
        ),
    ]
