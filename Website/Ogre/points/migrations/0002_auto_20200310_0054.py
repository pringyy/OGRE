# Generated by Django 2.1.7 on 2020-03-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='studentprofileinfo',
            name='profile_pic',
        ),
    ]
