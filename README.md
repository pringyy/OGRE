# University of Glasgow- Online Games and Resource Environment (OGRE)

This README file outlines all the functionality of this project, with an extensive installation guide. <br>
If you have any queries about anything to do with this application please contact us using our emails below.<br>
Before deploying the application, **please make sure you read through this entire document.** 

# Introduction


### Meet the team

*  Robert Pringle (*Team Leader*)- 2304777P@student.gla.ac.uk
*  Mingfeng Ye (*Product Checker*)- 2325714Y@student.gla.ac.uk
*  Alastair Innes (*Product Owner*)- 2317070I@student.gla.ac.uk
*  Catriona Murphy (*Note Taker*)- 2312695M@student.gla.ac.uk
*  Chung Ki Yau (*Product Demonstrator*)- 2359033Y@student.gla.ac.uk
*  Chutmongkon Chuasaard (*Team Coach*)- 2425143C@student.gla.ac.uk


### Requirements

This project has been created to motivate students to do University work. It does this by rewarding them with points that they can spend on cosmetic items. As we are working for a customer who is developing this idea, we were given a limited scope of requirements.


**Functional Requirements:**
*  The application must be able to track OGRE points, when users submit an assignment on moodle.
*  The application need to provide APIs for other games to observe and manipulate OGRE points
*  Provide a sample Unity videogame to demonstrate the application's API. 

**Non-Functional Requirements:**
*  Demonstration Unity videogame does not need to be interesting.
*  The application must have sufficient amount of security. (E.g. Can not give points randomly.)
*  The application does not need to comply with GDPR.
*  The application can use any extension (That they have the right to use, such as MIT license).
*  Have to make use of a database table to store point details

### Approach

We decided to approach this challenge by creating a mySQL table on a Moodle server which stores users points. Event listeners were then implemented which would update the table when users submit an assignment or quiz. From this we decided to create a Django web application which used API calls to link it with the Moodle server. The API calls allowed us to retrieve and update points on the mySQL table using the Django application. It also allowed us to set up a regitration system, which only allows you to register for the Django application if you are an existing user on the corresponding Moodle server. The Django applicaiton provides an interface for users to see and spend their OGRE points. They can spend them to play games or on cosmetic items. The cosmetic items and games we implemented are placeholders, as this is the aspects of the application our customers are working on.
# Features

* Ability to register to the Django applicstion if and only if the user is registered on the linked Moodle server
* User authentication system with secure password hashing
* Password reset via email link (reset via Moodle server)
* Responsive UI (mobile mode)
* Cross browser support

#### Login
* Lets users login using their Username, Student ID and Password
* Random background is displayed everytime the page is refreshed
* THE IMAGES COMMITED WE DO NOT OWN THE RIGHTS TO, THEY ARE SIMPLY A PLACE HOLDER MAKE SURE THEY ARE CHANGED BEFORE DEPLOYING APPLICATION
![Screenshot of login page](https://i.imgur.com/THzP6tu.png)

#### Registration
![Screenshot of the registration page](https://i.imgur.com/H8czMjd.png)

#### Dashboard

#### About
* See information about the development team
![Screenshot of about page](https://i.imgur.com/kTNNaQc.png)

#### Contact
* Contact form to send a message to the development team
![Screenshot of contact page](https://i.imgur.com/Jb8f427.png)

* How to reconfigure this for your own email:

#### FAQ
* Displays freuqently asked questions to the user if they have a query:
![Screenshot of FAQ page]

#### Profile
* Ability to view your profile and other user's profiles
*See your OGRE points
![Screenshot of contact page]

#### Games Page


#### Avatar Shop

#### Transaction History

# Installation Guide

### 1. Git

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


### 2. Django Application

**Step 2.1**: You need to have Python 3.7 installed onto your machine to run this application. Download the version for the Operating System you are using here: 
*  https://www.python.org/downloads/release/python-376/

**Step 2.2**: Check you have successfully installed the correct version of Python using the command in the console:
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


**Step 2.5**: Next you need to setup the Django database on your system, to do this run these two commands in the console one after the other:
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

### 3. Moodle Server
**Step 3.1**: we assume you have the moodle installed, and have the database and source code access and modify permission. If you do not have these, see link below for moodle installtion:
*  https://docs.moodle.org/38/en/Step-by-step_Installation_Guide_for_Ubuntu

**Step 3.2**: Next we need to access the moodle database, create two related table "mdl_user_points" and "mdl_user_points_trans", so enter the database mode by:
```
mysql -u <database_username> -p
```
*Then create that two table*

*mdl_user_points*
```
CREATE TABLE IF NOT EXISTS mdl_user_points (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    points INT NOT NULL
);
```
*mdl_user_points_trans*
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

**Step 3.3**: Once you have completed the setup above, you need to  replace and add some files in the moodle side:  

*1. replace the moodle/api/mod/quiz/locallib.php*

*with cs17-main/api/mod/quiz/locallib.php*

*2. replace the moodle/api/mod/assign/locallib.php*

*with cs17-main/api/mod/assign/locallib.php*

*3. move cs17-main/api directory*

*to moodle/*

### 4. Link Django with Moodle Server



```

Live server of Moodle server:
Live server of Django webapp: