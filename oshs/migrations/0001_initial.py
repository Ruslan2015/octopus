# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MacroDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('inbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshs.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='SubDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('inbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshs.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='inbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshs.MacroDepartment'),
        ),
    ]
