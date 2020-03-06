from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from django.test.client import Client

from .models import StudentProfileInfo, User
from .forms import UserForm, ContactForm, UserProfileInfoForm


class IndexPageTest(TestCase):

    # Page can only be used when user is logged in, so create user and log them in
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    # tests that login page uses login url
    def test_index_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    # tests that index page uses template
    def test_index_page_uses_templates(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'points/index.html')


class LoginPageTest(TestCase):
    # tests that login page uses login url
    def test_login_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    # tests that login page uses template
    def test_login_page_uses_templates(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'points/login.html')


class FAQPageTest(TestCase):
    # tests that faq page uses faq url
    def test_faq_view_url_by_name(self):
        response = self.client.get(reverse('faq'))
        self.assertEquals(response.status_code, 200)

    # tests that faq page uses template
    def test_faq_page_uses_templates(self):
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'points/faq.html')


class ProfilePageTest(TestCase):
    # tests that profile page uses profile url
    def test_profile_view_url_by_name(self):
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)

    # tests that profile page uses template
    def test_profile_page_uses_templates(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'points/profile.html')


class ThanksPageTest(TestCase):
    # tests that thanks page uses thanks url
    def test_thanks_view_url_by_name(self):
        response = self.client.get(reverse('thanks'))
        self.assertEquals(response.status_code, 200)

    # tests that contact page uses template
    def test_thanks_page_uses_templates(self):
        response = self.client.get(reverse('thanks'))
        self.assertTemplateUsed(response, 'points/thanks.html')


class ContactPageTest(TestCase):
    # tests that contact page uses contact url
    def test_contact_view_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)

    # tests that contact page uses template
    def test_contact_page_uses_templates(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'points/contact.html')

class RegisterPageTest(TestCase):
    # tests that register page uses register url
    def test_register_view_url_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    # tests that register page uses template
    def test_register_page_uses_templates(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'points/register.html')

class AboutPageTest(TestCase):
    # tests that about page uses about url
    def test_about_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

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


class StaticImageTests(TestCase):
    # tests that static images display correctly on the website
    def test_correct_static_images(self):

        images = {"jpg" : ['alastair', 'bg1', 'bg2', 'bg3', 'bg4',
                           'bg5', 'bg6', 'bg7', 'catoriona', 'harry',
                           'mingfeng', 'robert'],
                  "png" : ['ogrelogo', 'unilogo']}

        for format, file in images.items():
            for f in file:
                img = finders.find('images/{}.{}'.format(f, format))
                self.assertIsNotNone(img)

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

    # tests if the user form is invalid when given invalid data
    def test_user_form_invalid(self):
        form = UserForm(data={'studentID': "2317070i", 'email': "a@b.com", 'password': "password123"})
        self.assertFalse((form.is_valid()))

class ContactFormTests(TestCase):

    # tests if the contact form is valid when given valid data
    def test_contact_form_valid(self):
        form = ContactForm(data={'contact_name':'Test', 'contact_email': "a@b.com", "subject":"test", "content":"This is a test!"})
        self.assertTrue(form.is_valid())

    # tests if the contact form is invalid when given invalid data
    def test_user_form_invalid(self):
        form = ContactForm(data={'contact_email': "a@b.com", "subject":"test", "content":"This is a test!"})
        self.assertFalse((form.is_valid()))
