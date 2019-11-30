from django.db import models
from django.contrib.auth.models import User
class StudentProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	StudentID = models.CharField(unique=True,null=True,max_length = 8)
	currentPoints = models.IntegerField(default= 0)
	spentPoints = models.IntegerField(default= 0)
	totalPoints = models.IntegerField(default= 0)
	def __str__(self):
		return (self.user.username + ": "+self.StudentID)
