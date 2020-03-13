# Installation Guide

Please make sure you complete this **whole** guide for the application to work as intended.<br>
If anything in this guide is not clear or you have any issues or queries please [contact us](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/blob/develop/README.md#meet-the-team) on the information provided in the README.

## Contents

1. [Git Setup](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#1-git-setup)
2. [Django Application Setup](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#2-django-application-setup)
3. [Moodle Server Setup](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#3-moodle-server-setup)
4. [Django Application Configurations](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#4-django-application-configurations)
5. [Moodle Server Configurations](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#5-moodle-server-configurations)

## 1. Git Setup

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

 
## 2. Django Application Setup

**Step 2.1**: You need to have Python 3.7 installed onto your machine to run this application. Download the version for the Operating System you are using here: 
*  https://www.python.org/downloads/release/python-376/

**Step 2.2**: Check you have successfully installed the correct version of Python using the command in the console:
```
python --version
```
*If the wrong version is displayed, try uninstalling python and reinstalling it again via the link.*

**Step 2.3 *(Linux and Mac OS)***: Once you have completed the setup above, navigate to the 'cs17-main' folder on your terminal and run the following command:

```
pip install -r requirements
```

*This installs all the packages, including Django, at the correct version required for the application to work.*<br>
*Pip is a python package manager that automatically comes installed when you download Python 3.4 or above.*

**Step 2.3 *(Windows OS)*:** If you are trying the run the Django application locally on Windows, one of the requirements will NOT install correctly using Pip. You are going to have to download Anaconda on to your machine:
*  https://docs.anaconda.com/anaconda/install/

*Anaconda is a package manager like Pip that also allows you to set-up virtual environments locally.*

&nbsp;&nbsp;&nbsp;***Step 2.3.1 (Windows OS):*** Next you need to setup a virtual environment. Open the Anaconda Prompt application (should be installed alongside Anaconda) and input the following:

```
conda create -n [environment_name] python=3.7
```
&nbsp;&nbsp;&nbsp;*Replace '[environment_name]' with what you want your Virtual Environment to be called, but make sure you remember it!*

&nbsp;&nbsp;&nbsp;***Step 2.3.2 (Windows OS):***  Next navigate to the 'cs17-main' folder on Anaconda prompt and run the following commands in sequential order:
```
conda activate [environment_name]
pip install -r requirements
conda install pycrypto
```
&nbsp;&nbsp;&nbsp;*Make sure you replace '[environment_name]' with the name you defined in the Step 2.3.2*<br>
&nbsp;&nbsp;&nbsp;*Pycrypto is essential to install as it encrypts our API keys to make sure user sessions are valid between our application and the server.*

&nbsp;&nbsp;&nbsp;***Step 2.3.3 (Windows OS):*** Every time you wish to use the website, you must always ensure you activate the virtual environment in Anaconda promptlike so:
```
conda activate [environment_name]
```
&nbsp;&nbsp;&nbsp;*Make sure you replace '[environment_name]' with the name you defined in the Step 2.3.2*



**Step 2.4**: Next navigate into the directory where the actual Django application is being stored by entering the following into the console:
```
cd Website/Ogre
```


**Step 2.5**: Next you need to setup the Django database on your system, to do this run these two commands into the console in sequential order:
```
python manage.py makemigrations  

python manage.py migrate
```
*If this does not work make sure you are in the correct directory shown in Step 2.4*

**Step 2.6**: Now you will be able to run the Django server using:
```
python manage.py runserver
```
*To see the application you need navigate to the address displayed in the console on a web browser.*

**You WILL NOT be able to register or login until you complete the installation guide!**

## 3. Moodle Server Setup

**Step 3.1**: You need to have a running Moodle server to link the Django application. If you do not already have one running, you can follow this setup guide:
*  https://docs.moodle.org/38/en/Installing_Moodle

*The server CANNOT be local. It has to be on a server with a public IP address, so the Django application can access it*

**Step 3.2**: To create the Moodle mySQL Databases required, you must enter the database mode by entering the following into the console of the server:

```
mysql -u <database_username> -p
```
**Step 3.3** Now we are going to create the first table 'mdl_user_points' by entering the following SQL into the console of the server:

```
CREATE TABLE IF NOT EXISTS mdl_user_points (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    points INT NOT NULL
);
```
*If this does not work make sure you are in the database mode shown in Step 3.2*

**Step 3.4** Next create the next table 'mdl_user_points_trans' by entering the following SQL into the console of the server:

```
CREATE TABLE IF NOT EXISTS mdl_user_points_trans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    detail VARCHAR(50) NOT NULL,
    amount INT NOT NULL,
    user_id INT NOT NULL,
    spentTime DATE
);
```
*If this does not work make sure you are in the database mode shown in Step 3.2*

**Step 3.3**: Once you have completed the setup above, you need to  replace and add some files on the Moodle server:  


&nbsp;&nbsp;&nbsp;**Step 3.3.1:** replace the moodle/api/mod/quiz/locallib.php with cs17-main/api/mod/quiz/locallib.php

&nbsp;&nbsp;&nbsp;**Step 3.3.2:** replace the moodle/api/mod/assign/locallib.php with cs17-main/api/mod/assign/locallib.php

&nbsp;&nbsp;&nbsp;**Step 3.3.3** move cs17-main/api directory to moodle/

&nbsp;&nbsp;&nbsp;**Step 3.3.4** move cs17-main/api/include directory to moodle/


## 4. Django Application Configurations:

**Configuration 4.1:** Now you have to change the API calls on the Django application to link to your Moodle server.
*  On your repository open the file [cs17-main//Website/Ogre/points/APIcalls.py](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/blob/develop/Website/Ogre/points/APIcalls.py).
*  Here change the IP of the links, lines 5-11, to the IP of your Moodle server.
*  Make sure you only change the IP and keep the directories after the same and do not change any variables names.
*  This file is imported into views.py where the API calls are made.
*  You can find the views.py file at the following directory in your repository[cs17-main/Website/Ogre/points/views.py](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/blob/develop/Website/Ogre/points/views.py).


**Configuration 4.2:** Change forgotten password link to redirect to your Moodle server.
*  On your repository open the file [cs17-main/Website/Ogre/templates/points/login.html](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/blob/develop/Website/Ogre/templates/points/login.html).
*  Then navigate to line (ENTER LINE HERE).
*  Replace the link with the address to your Moodle servers reset password page.


**Configuration 4.3:** To put the application on to a live server, so anyone can access it via the internet please follow this guide:

*  https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

**Configuration 4.3 (optional):** How to change the cost of activities on the Web Application.
* On your repository open the file  [cs17-main/Website/Ogre/points/costValues.py](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/tree/develop/Website/Ogre/points/costValues.py).
* From here you can edit the integer values to change the cost of different activities on the application.  

**Configuration 4.4 (optional):** Change the email the contact page send emails to.
*  Our contact page ONLY works for a gmail account
*  WRITE MORE EXPLANATION

**Configuration 4.5 (optional):** Change the random backgrounds displayed on the login screen.
*  On your repository open the folder [cs17-main/Website/Ogre/static/images/loginBackground](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/tree/develop/Website/Ogre/static/images/loginBackground)
*  Here is where you can import your own images and remove the placeholder ones.
*  They HAVE to be called 'bg' followed by a number between 1 and 5, e.g. 'bg2', 'bg3'.
*  They also HAVE to be .jpg files and in the default configuration there MUST be 5 pictures.
*  If you want to change the number of random pictures displayed navigate to []()
*  Change the number on line to the number of images you have subract one, so if you have 20 images enter 19 here.
*  WRITE MORE EXPLANATION

**Configuration 4.6 (optional):** How to change API encryption keys

**Configuration 4.7 (optional):** You can configure our Django application further in many different ways. If you are unfamiliar with how to do so, I would study these guides to understand how the technologies we use work to make additonal changes to our implementation:
*  [See Django guide](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
*  [See HTML guide](https://html.com/)
*  [See CSS guide](https://www.w3schools.com/css/)
*  [See Bootstrap4 guide](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
*  [See Java Script guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
*  [See Ajax guide](https://www.w3schools.com/xml/ajax_intro.asp)
*  [See JQuery guide](https://www.w3schools.com/jquery/)


## 5. Moodle Server Configurations:

**Configuration 5.1:** How to change how much 'OGRE' points users are rewarded for carrying out tasks:
* Open the "togglecompletion.php" file on the moodle server.
* Navigate to line (ENTER LINE HERE ONCE COMMENTS ARE DONE).
* Here if you change the integer values it will change how many points users are given for submitting different assignments.

**Configuration 5.2:** If you want to make changes to the Moodle server like creating a course, enrolling users in a course and setting up assignments for those courses please follow this guide:
*  [See Moodle guide](https://docs.moodle.org/38/en/Admin_quick_guide#Adding_users) for adding users.
*  [See Moodle guide](https://docs.moodle.org/38/en/Admin_quick_guide#Adding_users) for adding courses.
*  [See Moodle guide](https://docs.moodle.org/38/en/Admin_quick_guide#Adding_users) for enrolling users on to courses.
*  [See Moodle guide](https://docs.moodle.org/38/en/Assignment_quick_guide) for adding assignments to the courses.

**Configuration 5.3:** If you want to make any further changes to our API code, and you are unfamilar with PHP we would recommend to follow this guide:
*  [See PHP guide](https://www.w3schools.com/php/).

