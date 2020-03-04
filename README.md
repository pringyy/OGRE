This is a project that uses a Django web application to connect to an external 
Moodle server so users can log in and see their "ORGE Points" - a point system
that works with Moodle to reward users for submitting assignments and completing
quizes.

## Installation

### Django Application Setup

First clone the repository and then navigate to the Ogre source folder.

You must have must have a Python 3.7 virtual environment installed on your machine for this to work.

Here is a comprehensive guide on how to setup Django on your machine to run the application: https://tinyurl.com/DjangoSetupGuide

You must run these commands in order for the application to work and must make sure:

```
pip install -r requirements.txt //This installs all the APIs at the correct version required for the application to work

python manage.py makemigrations  

python manage.py migrate
```

### Moodle Server setup

## Feautures
* Ability to register to the Django applicstion if and only if the user is registered on the linked Moodle server
* User authentication system with secure password hashing
* Password reset via email link (reset via Moodle server)
* Google Maps integration
* Responsive UI (mobile mode)
* Cross browser support

#### Login
* Lets user login using Username, Student ID and Password
* Random background is displayed everytime the page is refreshed

#### About
* See information about the development team
![Screenshot of about page]

#### Contact
* Contact form to send a message to the development team
![Screenshot of contact page]

* How to reconfigure this for your own email:


#### FAQ
* Displays freuqently asked questions to the user if they have a query:
![Screenshot of FAQ page]

#### Profile
* Ability to view your profile and other user's profiles
*See your OGRE points
![Screenshot of contact page]


```

To run on your own machine, you must have a Python 3.7 virtual environemnt with
the following apis installed:

autograd==1.3

certifi==2019.9.11

Django==2.2.7

Pillow==6.2.1

pylev==1.3.0

pytz==2019.3

sqlparse==0.3.0

wincertstore==0.2

To install these, run pip install -r requirements.txt

Live server of Moodle server:
Live server of Django webapp: