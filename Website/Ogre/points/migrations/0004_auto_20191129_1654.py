# Generated by Django 2.1.7 on 2019-11-29 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0003_auto_20191113_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('StudentID', models.IntegerField(unique=True)),
                ('currentPoints', models.IntegerField(default=0)),
                ('spentPoints', models.IntegerField(default=0)),
                ('totalPoints', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
