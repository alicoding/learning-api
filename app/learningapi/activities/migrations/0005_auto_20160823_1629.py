# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20160818_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityTeachingKit',
            new_name='TeachingKitActivity',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='weblitskills',
            new_name='weblit_skills',
        ),
    ]