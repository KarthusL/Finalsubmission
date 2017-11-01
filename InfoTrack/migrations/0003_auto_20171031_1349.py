# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoTrack', '0002_auto_20171029_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentinstance',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='postinstance',
            name='post',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['time']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['time']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='CommentInstance',
        ),
        migrations.DeleteModel(
            name='PostInstance',
        ),
    ]