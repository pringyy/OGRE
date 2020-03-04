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
*This will save the repository into whatever directory you navigated into in Step 1.2.*


### Step 2: Django Application

**Step 2.1**: You need to have Python 3.7 installed onto your machine to run this application. Download the version for the Operating System you are using here: 
*  https://www.python.org/downloads/release/python-376/

**Step 2.2**: Check you have successfully installed the correct version of Python using the command:
```
python --version
```
*If the wrong version is displayed, try uninstalling python and reinstalling it again via the link.*

**Step 2.3**: Once you have completed the setup above, navigate to the 'cs17-main' folder on your terminal and run the following command:

```
pip install -r requirements
```
*This installs all the packages, including Django, at the correct version required for the application to work.*<br>
*Pip is a python package manager that automatically comes installed when you download Python 3.4 or above.*

**Step 2.4**: Next navigate into the directory where the actual Django application is being stored by entering the following into the console:
```
cd website/Ogre
```


**Step 2.5**: Next you need to setup the Django database on your system, to do this run these two commands one after the other:
```
python manage.py makemigrations  

python manage.py migrate
```

**Step 2.6**: Now you will be able to run the Django server using:
```
python manage.py runserver
```
*To see the application you need navigate to the address displayed in the console on a web browser.*

**You WILL NOT be able to register or login until you complete the installation guide!**

### Step 3: Moodle Server


### Step 4: Link Django with Moodle Server

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