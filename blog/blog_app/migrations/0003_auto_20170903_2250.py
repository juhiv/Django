# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 17:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 9, 3, 17, 20, 24, 506852, tzinfo=utc)),
            preserve_default=False,
        ),
    ]