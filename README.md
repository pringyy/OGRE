# University of Glasgow- Online Games and Resource Environment (OGRE)

This README file outlines all the functionality of this project, with an extensive installation guide. <br>
If you have any queries about anything to do with this application please contact us using our emails below.<br>
Before deploying the application, **please make sure you read through this entire document.** 

## Installation Guide

See [Installation Guide](INSTALLATIONGUIDE.md)

## License
See [License](LICENSE.md)


## Introduction


#### Meet the team

*  Robert Pringle (*Team Leader*)- 2304777P@student.gla.ac.uk
*  Mingfeng Ye (*Product Checker*)- 2325714Y@student.gla.ac.uk
*  Alastair Innes (*Product Owner*)- 2317070I@student.gla.ac.uk
*  Catriona Murphy (*Note Taker*)- 2312695M@student.gla.ac.uk
*  Chung Ki Yau (*Product Demonstrator*)- 2359033Y@student.gla.ac.uk
*  Chutmongkon Chuasaard (*Team Coach*)- 2425143C@student.gla.ac.uk


#### Requirements

This project has been created to motivate students to do University work. It does this by rewarding them with points that they can spend on cosmetic items. As we are working for a customer who is developing this idea, we were given a limited scope of requirements.


*Functional Requirements:*
*  The application must be able to track OGRE points, when users submit an assignment on moodle.
*  The application need to provide APIs for other games to observe and manipulate OGRE points
*  Provide a sample Unity videogame to demonstrate the application's API. 

*Non-Functional Requirements:*
*  Demonstration Unity videogame does not need to be interesting.
*  The application must have sufficient amount of security. (E.g. Can not give points randomly.)
*  The application does not need to comply with GDPR.
*  The application can use any extension (That they have the right to use, such as MIT license).
*  Have to make use of a database table to store point details

#### Approach

We decided to approach this challenge by creating a mySQL table on a Moodle server which stores users points. Event listeners were then implemented which would update the table when users submit an assignment or quiz. From this we decided to create a Django web application which used API calls to link it with the Moodle server. The API calls allowed us to retrieve and update points on the mySQL table using the Django application. It also allowed us to set up a regitration system, which only allows you to register for the Django application if you are an existing user on the corresponding Moodle server. The Django applicaiton provides an interface for users to see and spend their OGRE points. They can spend them to play games or on cosmetic items. The cosmetic items and games we implemented are placeholders, as this is the aspects of the application our customers are working on.

## Features

* Responsive UI (mobile mode)
* Cross browser support
* Navigation bar displayed on all webpages except the Login/Launch page

#### Login/Launch screen

* First interface the user interacts with when application is opened.
* User authentication system with secure password hashing.
* Users login using three fields of information: Username, Student ID and Password.
* Random background is displayed everytime the page is refreshed.
* Password reset via email link (reset via Moodle server).
![Screenshot of login page](https://i.imgur.com/THzP6tu.png)

#### Registration

* Only lets user register to the Django application if and only if the user is registered on the corresponding Moodle server.
* Does this by checking Student ID and Password entered  match an user ID and corresponding password on the Moodle server.
* Lets users decide a username or 'nickname' for the application.
![Screenshot of the registration page](https://i.imgur.com/H8czMjd.png)

#### Dashboard

* Main menu of the application.
* Users can see how many points they currently have.
*![Screenshot of the dashboard](https://i.imgur.com/qXh9Jb5.png)

#### About

* See information about the development team
![Screenshot of about page](https://i.imgur.com/kTNNaQc.png)

#### Contact

* Contact form to send a message to the development team
![Screenshot of contact page](https://i.imgur.com/Jb8f427.png)

#### FAQ

* Displays freuqently asked questions to the user.
![Screenshot of FAQ page]

#### Profile

* Ability to view your profile.
* See your OGRE points and account information.
![Screenshot of  profile page](https://i.imgur.com/gVd2C2Q.png)

#### Leaderboard
![Screenshot of the leaderboard](https://i.imgur.com/lYkhZPQ.png)

#### Games
* Lets users play game that cost 5 points to play.
![Screenshot of games list page](https://i.imgur.com/6V0lTaf.png)


#### Avatar Shop

#### Transaction History
![Screenshot of the transaction history page](https://i.imgur.com/4druPxc.png)



