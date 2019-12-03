import time, uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='profile_images', blank=True)
    options = models.TextField(default='null')

    current_points = models.IntegerField(default=0)
    spent_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

