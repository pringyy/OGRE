# Generated by Django 3.0.2 on 2020-02-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0006_auto_20200219_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofileinfo',
            name='currentPoints',
        ),
        migrations.RemoveField(
            model_name='studentprofileinfo',
            name='spentPoints',
        ),
        migrations.RemoveField(
            model_name='studentprofileinfo',
            name='totalPoints',
        ),
    ]