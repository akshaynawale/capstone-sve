# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfv', '0004_auto_20170404_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instances',
            old_name='ImageName',
            new_name='Image',
        ),
    ]