# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfv', '0002_remove_images_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='Repo',
            field=models.CharField(default='NONE', max_length=200),
        ),
    ]