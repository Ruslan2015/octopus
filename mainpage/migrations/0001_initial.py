# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpCoordTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('pubdate', models.DateTimeField()),
                ('listworkers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MpDeadlineTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('worker', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MpDeadlineWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('project', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('daedline', models.DateTimeField()),
                ('worker', models.CharField(max_length=250)),
            ],
        ),
    ]
