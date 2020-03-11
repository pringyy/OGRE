# Installation Guide

Please make sure you complete this **whole** guide for the application to work as intended.
## Contents

1. [Git](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#1-git)
2. [Django Application](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#2-django-application)
3. [Moodle Server](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#3-moodle-server)
4. [Link Django Application with Moodle server](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#4-link-django-with-moodle-server)
5. [Further Django Setup](https://stgit.dcs.gla.ac.uk/tp3-2019-cs17/cs17-main/-/edit/develop/INSTALLATIONGUIDE.md#5-further-django-setup)

## 1. Git

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


## 2. Django Application

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

## 3. Moodle Server

**Step 3.1**: You need to have a running Moodle server to link the Django application. If you do not already have one running, you can follow this setup guide:
*  https://docs.moodle.org/38/en/Installing_Moodle

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

**Step 3.3**: Once you have completed the setup above, you need to  replace and add some files in the moodle side:  

*1. replace the moodle/api/mod/quiz/locallib.php*

*with cs17-main/api/mod/quiz/locallib.php*

*2. replace the moodle/api/mod/assign/locallib.php*

*with cs17-main/api/mod/assign/locallib.php*

*3. move cs17-main/api directory*

*to moodle/*

*4. move cs17-main/api/include directory*

*to moodle/*

## 4. Link Django with Moodle Server

## 5. Further Django Setup


```

Live server of Moodle server:
Live server of Django webapp: