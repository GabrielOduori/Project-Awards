# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(),
        ),
    ]
