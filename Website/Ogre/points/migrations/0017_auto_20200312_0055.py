# Generated by Django 2.1.7 on 2020-03-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0016_auto_20200312_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofileinfo',
            name='profile_pic',
            field=models.ImageField(default='avatar-default-icon.png', upload_to=''),
        ),
    ]