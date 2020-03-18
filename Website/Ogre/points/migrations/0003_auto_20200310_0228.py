# Generated by Django 2.1.7 on 2020-03-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20200310_0054'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentAvatar',
        ),
        migrations.AddField(
            model_name='studentprofileinfo',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/avatar-default-icon.png', upload_to='profile_pics'),
        ),
    ]
