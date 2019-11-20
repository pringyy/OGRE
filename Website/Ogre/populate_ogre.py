import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ogre.settings')

import django

django.setup()

from points.models import Student


def populate():
    students = [{"StudentID": "2317070i", "spentPoints": 20, "totalPoints": 70},
                {"StudentID": "2317670k", "spentPoints": 0, "totalPoints": 70},
                {"StudentID": "2317890i", "spentPoints": 50, "totalPoints": 200},
                {"StudentID": "2323985k", "spentPoints": 0, "totalPoints": 0}]

    for student in students:
        studentID = student["StudentID"]
        total = student["totalPoints"]
        spent = student["spentPoints"]
        current = total - spent

        


