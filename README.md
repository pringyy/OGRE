# University of Glasgow- Online Games and Resource Environment (OGRE)

This README file outlines all the functionality of this project, with an extensive installation guide. <br>
If you have any queries about anything to do with this application please contact us using our emails below.<br>
Before deploying the application, **please make sure you read through this entire document.** 

# Installation Guide

Click here to navigate to the Installation Guide:

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

