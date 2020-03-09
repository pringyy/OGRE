from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from .models import StudentProfileInfo, User
from .forms import UserForm, ContactForm, UserProfileInfoForm


class IndexPageTest(TestCase):

    # Page can only be used when user is logged in, so create user and log them in
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        self.client.login(username='test', password='testpassword')

        self.response = self.client.get(reverse('index'))

    # tests that login page uses login url
    def test_index_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that index page uses template
    def test_index_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/index.html')

    # tests that the index page displays a users points to them
    def test_index_page_displays_points(self):
        self.assertContains(self.response, 'Points')

    # tests that user can't see index page when logged out
    def test_index_page_restricted_when_logged_out(self):
        # Log user out and obtain response again
        self.client.logout()
        self.response = self.client.get(reverse('index'))

        self.assertEquals(self.response.status_code, 302)


class LoginPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('login'))

    # tests that login page uses login url
    def test_login_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that login page uses template
    def test_login_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/login.html')

    def test_login_page_has_required_fields(self):
        self.assertContains(self.response, 'StudentID')
        self.assertContains(self.response, 'Password')
        self.assertContains(self.response, 'Username')

    # tests that login page contains sign in button
    def test_login_page_has_sign_in_button(self):
        self.assertContains(self.response, "Sign in")

    # tests that login page contains register button
    def test_login_page_has_register_button(self):
        self.assertContains(self.response, "Register here")


class FAQPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('faq'))

    # tests that faq page uses faq url
    def test_faq_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that faq page uses template
    def test_faq_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/faq.html')


class ProfilePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        self.client.login(username='test', password='testpassword')

        self.response = self.client.get(reverse('profile'))

    # tests that profile page uses profile url
    def test_profile_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that profile page uses template
    def test_profile_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/profile.html')

    # tests that profile page displays points
    def test_profile_page_displays_points(self):
        self.assertContains(self.response, "Total Points")


class ThanksPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('thanks'))

    # tests that thanks page uses thanks url
    def test_thanks_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that thanks page uses template
    def test_thanks_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/thanks.html')

    # tests that thanks page displays thank you message
    def test_thanks_pages_provides_message(self):
        self.assertContains(self.response, 'Thanks for submitting the contact form!')


class ContactPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('contact'))

    # tests that contact page uses contact url
    def test_contact_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that contact page uses template
    def test_contact_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/contact.html')


class RegisterPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('register'))

    # tests that register page uses register url
    def test_register_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that register page uses template
    def test_register_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/register.html')

    def test_register_page_has_required_fields(self):
        self.assertContains(self.response, 'StudentID')
        self.assertContains(self.response, 'Password')
        self.assertContains(self.response, 'Username')

    # tests that login page contains register button
    def test_register_page_has_register_button(self):
        self.assertContains(self.response, "Register")


class AboutPageTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    # tests that about page uses about url
    def test_about_view_url_by_name(self):
        self.assertEquals(self.response.status_code, 200)

    # tests that about page uses template
    def test_about_page_uses_templates(self):
        self.assertTemplateUsed(self.response, 'points/about.html')

    def test_about_page_has_title(self):
        self.assertIn(b'<title>', self.response.content)
        self.assertIn(b'</title>', self.response.content)

    # tests that the about page correctly displays the name of the staff
    def test_about_page_contains_staff(self):
        self.assertIn(b'Alastair Innes', self.response.content)
        self.assertIn(b'Robert Pringle', self.response.content)
        self.assertIn(b'Catriona Murphy', self.response.content)
        self.assertIn(b'Mingfeng Ye', self.response.content)
        self.assertIn(b'Harry Yau', self.response.content)


class StaticImageTests(TestCase):
    # tests that static images display correctly on the website
    def test_correct_static_images(self):

        # Create dict mapping each file format to a list of the photos of that kind
        images = {"jpg": ['alastair', 'bg1', 'bg2', 'bg3', 'bg4',
                          'bg5', 'bg6', 'bg7', 'catoriona', 'harry',
                          'mingfeng', 'robert'],
                  "png": ['ogrelogo', 'unilogo']}

        # Check that each image exists in th website
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
        form = UserForm(
            data={'username': "user123", 'password': "password123"})
        self.assertTrue(form.is_valid())

    # tests if the user form is invalid when given invalid data
    def test_user_form_invalid(self):
        form = UserForm(data={'studentID': "2317070i", 'password': "password123"})
        self.assertFalse(form.is_valid())


class UserProfileInfoFormTests(TestCase):

    # tests is the user profile form is valid when given valid data
    def test_user_profile_info_form(self):
        form = UserProfileInfoForm(data={"StudentID": "2317070i", "profile_pic": "test.jpg"})
        self.assertTrue(form.is_valid())

    # tests if the user profile form is valid with no profile picture provided
    def test_user_profile_info_form_with_no_profile_pic(self):
        form = UserProfileInfoForm(data={"StudentID": "2317070i"})
        self.assertTrue(form.is_valid())

    # tests if the user profile form is invalid when given invalid data
    def test_user_profile_form_invalid(self):
        form = UserForm(data={'password': "password123"})
        self.assertFalse(form.is_valid())


class ContactFormTests(TestCase):

    # tests if the contact form is valid when given valid data
    def test_contact_form_valid(self):
        form = ContactForm(
            data={'contact_name': 'Test', 'contact_email': "a@b.com", "subject": "test", "content": "This is a test!"})
        self.assertTrue(form.is_valid())

    # tests if the contact form is invalid when given invalid data
    def test_contact_form_invalid(self):
        form = ContactForm(data={'contact_email': "a@b.com", "subject": "test", "content": "This is a test!"})
        self.assertFalse((form.is_valid()))
