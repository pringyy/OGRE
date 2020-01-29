from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from django.test import LiveServerTestCase
from .models import StudentProfileInfo, User
from .forms import UserForm

class LoginPageTest(TestCase):

    # tests that login page uses template
    def test_login_page_uses_templates(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'points/login.html')

    def test_login_page_has_title(self):
        response = self.client.get(reverse('login'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)

class FAQPageTest(TestCase):

    # tests that faq page uses template
    def test_faq_page_uses_templates(self):
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'points/faq.html')

class ContactPageTest(TestCase):

    # tests that contact page uses template
    def test_contact_page_uses_templates(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'points/contact.html')

class RegisterPageTest(TestCase):

    # tests that register page uses template
    def test_faq_page_uses_templates(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'points/register.html')

class AboutPageTest(TestCase):

    # tests that about page uses template
    def test_about_page_uses_templates(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'points/about.html')

    def test_about_page_has_title(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)

    # tests that the about page correctly displays the name of the staff
    def test_about_page_contains_staff(self):
        response = self.client.get(reverse('about'))

        self.assertIn(b'Alastair Innes', response.content)
        self.assertIn(b'Robert Pringle', response.content)
        self.assertIn(b'Catriona Murphy', response.content)
        self.assertIn(b'Mingfeng Ye', response.content)
        self.assertIn(b'Harry Yau', response.content)

'''
class StaticImageTests(TestCase):

    # tests that static images display correctly on the website
    def test_correct_static_images(self):

        jpgs = ['alastair', 'background', 'catoriona', 'harry', 'mingfeng', 'robert']
        pngs = ['ogrelogo', 'unilogo']

        for j in jpgs:
            img = finders.find('images/{}.jpg'.format(j))
            self.assertIsNotNone(img)

        for p in pngs:
            img = finders.find('images/{}.png'.format(p))
            self.assertIsNotNone(img)
'''

class StudentProfileTests(TestCase):

    def test_student_profile(self):

        # create User object
        User = get_user_model()
        user = User.objects.create_user('allyinnes99', '2317070i@student.gla.ac.uk', 'bad_password')

        # create Student object
        student = StudentProfileInfo()
        student.user = user
        student.StudentID = '2317070i'
        student.spentPoints = 50
        student.totalPoints = 150
        student.currentPoints = student.totalPoints - student.spentPoints

        student.save()

        record = StudentProfileInfo.objects.get(pk=1)
        self.assertEqual(record, student)

class UserFormTests(TestCase):

    # tests if the user form is valid when given valid data
    def test_user_form_valid(self):
        form = UserForm(data={'username': "user123", 'studentID': "2317070i", 'email': "a@b.com", 'password': "password123"})
        self.assertTrue(form.is_valid())

