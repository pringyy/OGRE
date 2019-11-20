from django.db import models

class Student(models.Model):
    StudentID = models.IntegerField(unique=True)
    currentPoints = models.IntegerField(default=0)
    spentPoints = models.IntegerField(default=0)
    totalPoints = models.IntegerField(default=0)

    def __str__(self):
        return self.StudentID
