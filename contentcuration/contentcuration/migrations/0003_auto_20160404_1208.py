# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('contentcuration', '0002_contentlicense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentlicense',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contentlicense',
            name='name',
        ),
        migrations.AddField(
            model_name='contentlicense',
            name='license_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.License'),
            preserve_default=False,
        ),
    ]
