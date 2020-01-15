from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from django.test import LiveServerTestCase


class LoginPageTest(TestCase):

    # tests that login page uses template
    def test_login_page_uses_templates(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'points/login.html')

    def test_login_page_has_title(self):
        response = self.client.get(reverse('login'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTest(TestCase):

    # tests that login page uses template
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

        jpgs = ['alastair', 'background', 'catoriona', 'harry', 'mingfeng', 'robert']
        pngs = ['ogrelogo', 'unilogo']

        for j in jpgs:
            img = finders.find('images/{}.jpg'.format(j))
            self.assertIsNotNone(img)

        for p in pngs:
            img = finders.find('images/{}.png'.format(p))
            self.assertIsNotNone(img)

