# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import multiuploader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiuploaderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(max_length=255, upload_to=multiuploader.models._upload_to)),
            ],
            options={
                'verbose_name': 'multiuploader file',
                'verbose_name_plural': 'multiuploader files',
            },
        ),
    ]
