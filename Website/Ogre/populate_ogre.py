import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Ogre.settings')

import django
django.setup()

from points.models import UserProfile
from django.contrib.auth.models import User


def populate():
    students = [{"email": "2317070i@student.gla.ac.uk", "password": "abc", "spentPoints": 20, "totalPoints": 70},
                {"email": "2317670k@student.gla.ac.uk", "password": "abc", "spentPoints": 0, "totalPoints": 70},
                {"email": "2317890i@student.gla.ac.uk", "password": "abc", "spentPoints": 50, "totalPoints": 200},
                {"email": "2323985k@student.gla.ac.uk", "password": "abc", "spentPoints": 0, "totalPoints": 0}]

    for student in students:
        email = student["email"]
        student_id = email.replace("@student.gla.ac.uk", "")
        total = student["totalPoints"]
        spent = student["spentPoints"]
        current = total - spent

        # ensure points are valid before creating object
        if current >= 0:
            add_student(student_id, current, spent, total)


def add_user(student_id, email, password):
    return UserProfile.objects.get_or_create(username=student_id, email=email, password=password)[0]


# add a new student model
def add_student(student_id, email, password, total, spent, current):
    userObject = add_user(student_id, email, password)

    s = \
    UserProfile.objects.get_or_create(user=userObject, total_points=total, current_points=current, spent_points=spent)[
        0]
    userObject = s.user
    total_points = s.total_points
    spent_points = s.spent_points
    current_points = s.current_points

    return s

# run script
if __name__ == '__main__':
	print("Starting Ogre population script...")
	populate()