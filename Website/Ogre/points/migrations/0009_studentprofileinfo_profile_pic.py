# Generated by Django 2.1.7 on 2020-02-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0008_remove_studentprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]