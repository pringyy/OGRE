import time, uuid
from django.db import models
from django.contrib.auth.models import User

#Used to represent the Student database model
class StudentProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images',default="images/avatar-default-icon.png")
    StudentID = models.CharField(unique=True,null=True,max_length = 8,help_text='Please enter your Student ID you use for Moodle.')
    def __str__(self):
        return (self.user.username)