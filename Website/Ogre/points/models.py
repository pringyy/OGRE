import time, uuid
from django.db import models
from django.contrib.auth.models import User
class StudentProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    StudentID = models.CharField(unique=True,null=True,max_length = 8,help_text='Required. the StudentID must your moodle studentID')
    def __str__(self):
        return (self.user.username)