# Generated by Django 2.1.7 on 2019-11-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0005_auto_20191130_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofileinfo',
            name='StudentID',
            field=models.CharField(max_length=7, null=True, unique=True),
        ),
    ]
