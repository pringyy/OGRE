This is a project that uses a Django web application to connect to an external 
Moodle server so users can log in and see their "ORGE Points" - a point system
that works with Moodle to reward users for submitting assignments and completing
quizes.

## Installation

### Step 1: Git

**Step 1.1**: To clone this repository through the console, you have to have Git installed on your machine:

*  Mac OS X setup guide: https://www.atlassian.com/git/tutorials/install-git#mac-os-x
*  Windows setup guide: https://www.atlassian.com/git/tutorials/install-git#windows
*  Linux setup guide: https://www.atlassian.com/git/tutorials/install-git#linux

**Step 1.2**: Once the setup has been completed navigate to the folder on the console where you want the repository to be cloned to, ``for example``:
```
cd Desktop/
```

*This would open the desktop directory in the console.*


**Step 1.3**: Clone the repository by using the following command in console:
```
git clone https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main.git
```
*This will save the repository into whatever directory you navigted to in Step 2.*


### Step 2: Django Application



You must have must have a Python 3.7 virtual environment installed on your machine for this to work.

Here is the official guide on how to setup Django on your machine to run the application: https://tinyurl.com/DjangoSetupGuide

Once you have completed the setup above, navigate to the 'cs17-main' folder on your terminal and run the following command:

```
pip install -r requirements
```
This installs all the APIs we use at the correct version required for the application to work.
```
python manage.py makemigrations  

python manage.py migrate
```

Now you will be able to run the server using:
```
python manage.py runserver
```

**You WILL NOT be able to register or login until you complete the next part of the installation guide!**

### Step 3: Moodle Server

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

Live server of Moodle server:
Live server of Django webapp: