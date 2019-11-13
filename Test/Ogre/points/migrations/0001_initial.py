# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-13 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField(unique=True)),
                ('team', models.IntegerField(unique=True)),
                ('currentPoints', models.IntegerField(default=0)),
                ('spentPoints', models.IntegerField(default=0)),
                ('totalPoints', models.IntegerField(default=0)),
            ],
        ),
    ]
