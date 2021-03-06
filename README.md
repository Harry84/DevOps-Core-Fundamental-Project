# DevOps-Core-Fundamental-Project: 
## Harry Potter Sorting Hat

### Contents

---

* [Introduction](#introduction)
* [Approach](#approach)
* [Starting Out](#starting-out)
* [ERD](#entity-relationship-diagram)
* [Table Relationship](#table-relationship)
* [User Stories](#user-stories)
* [CRUD Functionality](#crud-functionality)
* [Risk Analysis](#risk-analysis)
* [Unit Testing](#unit-testing)
* [Jenkins and Automation](#jenkins)
* [Test Analysis](#test-analysis)
* [Front End Design](#front-end)
* [Version Control](#version-control)
* [Possible Future Development](#future-dev)
* [Acknowledgements](#acknowledgements)

---

<a name="introduction"></a>
### Introduction

This is a basic web app intended to allow users (aka Hogwarts Students) to register their attendance of one of the four houses at Hogwarts.

As an MVP, two tables will be included in a relational db: one for houses and a second for student names.  These two tables will share a one to many relationship.  Users enter their name via a form and select a house to join.  Their name is then appended to a list of students within that house which they can then see displayed on a roster/home page along with the names of students in the other houses.

Ideally I will try to include a random element to assign houses (sorting hat) to prospective students and potentially will extend to include another table, student 
years.

---

<a name="approach"></a>
### Approach

I aim to use an agile approach in carrying out this project.  I will interpret user stories corresponding to my understanding of the MVP
and how it applies here.  On a daily basis, I will then set tasks to enable these user stories.  Given the short 
turnaround time of the project I will view each day as its own sprint and try to allocate tasks to my Trello board in the morning, as well 
updating the backlog, sprint backlog and completed sprint at the end of each day.

---

<a name="starting-out"></a>
### Starting out

* I decided to use Trello from the get go to help with planning and prioritisation.  Each day is treated as a sprint with its own backlog.  At the end of the day I move the completed task cards over to the completed sprint section of the board on the right hand side (see image below).

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Trello%20Board%20Day1.JPG" width="800"/>
</p>

[Link to Trello Board](https://trello.com/invite/b/rHR887uJ/b3f5c7e0b5ef60eb9c39ccbd42b3cae5/agile-sprint-board)

* Day 1 was a setup and planning day mainly - you can see roughly what I achieved in the completed tasks on the Trello board image above and how that compares to the most recent Trello board.
* Decided to simplify my project to something that was one to many - came up with this Harry Potter Houses idea.
* Signed up for drawio and did a basic sketch of the table relationships between students, houses and years (should I have time to include student year)

<a name="entity-relationship-diagram"></a>
### Entity Relationship Diagram:


<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Hogwarts%20Houses%20ERD.drawio.png" width="800"/>
</p>

<a name="table-relationship"></a>
### Table relationship

The two tables I include are Students and Houses - they share a one to many relationship in that Houses may have many students but each student may only be in one house.  This is shown symbolically via the line linking house_id within the Student table to house_id in the Houses table.   Each house can have many students, therefore the connecting line branches where it meets the Houses table.  Each student can only have one house, denoted by the single branch where the line meets the Students table.  Each student record has a house_id corresponding to the id of that student's house.  House_id is the primary key in the Houses table and the foreign key in the Students table.  A Years table is something that could be developed in future.

* Devised user stories - I decided to consider the examiner user story as a key one - after all the purpose of this project is to assess our progress and to be a quality gate therefore that is the most important user story - a collection of must haves!  This isn't intended at this stage to be an app that is used widely.

---

<a name="user-stories"></a>
### User Stories

_Must Haves:_

Must meet MVP definition: a project that satisfies the minimum passing requirements of the assignment:

* As the examiner I want to see the following evidenced in the project in order that it may pass:


    1. Kanban Board: Trello or an equivalent Kanban Board 
    2. At least 2 tables that share a relationship
    3. Database: GCP SQL Server or other Cloud Hosted managed Database
    4. CRUD functionality
    5. Programming language: Python
    6. Unit Testing with Python (Pytest) - test coverage includes most import areas - basic functions tested
    7. Some analysis of what was tested and why - summary of overall results present
    8. Front-end: Flask (HTML)
    9. Version Control: Git
    10. CI Server: Jenkins - build server was installed and used to produce a build
    11. Tests meet integration test spec - test should be able to verify if the application can access the database
    12. Cloud server: GCP Compute Engine
    13. A structured README.md along with relevant content
    14. Tools and workflows discussed in the documentation are implemented throughout the project
    15. Simple Risk Analysis performed


* As a student I want to be able to input my name, year and house into a form such that
it is stored on a database and I can access it at a later date.  i.e. create a student record

* As a user/student/teacher I want to be able to enter multiple students into the database for the
same reason. i.e. create multiple records which are appended.

* As a user I want to be able to see all the students and their corresponding houses and years
displayed in one place. i.e. retrieve all records from the db and have the info displayed on a webpage

* As a user I want to be able to update a student record

* As a user I want to be able to delete a student record

* As the examiner I would like to test that most or all of the above CRUD functionality is possible via automated tests


_Should Have:_

* As a user I want to be able to enter the name of one student and see their details displayed
alone.

* As a teacher I want to be able to update the name or house for any particular student

* As a student I want to know other students can't amend or delete my personal records

* As a teacher/admin I want to be able to amend or delete any student's records


_Could have:_

* Ages of students
* Last names of students
* Sorting hat option for random house assignment
* Some sort of sorting hat gif?
* Another table - many to many


_Won't have:_

* A good looking front end
* Much CSS or JS
* Much interactivity for a user
* A login system

--- 

<a name="crud-functionality"></a>
### CRUD Functionality

Using Flask and SQLAlchemy, I instantiate a db object using:

db = SQLAlchemy(app) in the init file.

I define the classes I want to use in models.py.  Each class has attributes which in turn form the columns of the db.  New entities are then instantiated in python via providing arguments to these classes.  These are only currently objects in Python.  In order to add them to the database I add and commit them. Please see routes.py for examples of the following:

* Create:
    Students and Houses are created
* Read:
    Student and House table entries are read
* Update:
    Student name and House entries can be updated.  House name entries can be updated.
* Delete:
    Student and House entries can be deleted.
    
---

<a name="risk-analysis"></a>
### Risk Analysis

My risk assessment attempts to identify potential threats to the integrity and future success of the project both in its function as a quality gate to be assessed on and as a pseudo app to be deployed in the public domain.  Control Measures are implemented and or proposed in order to protect against these perceived threats or risks.

Please click image below for larger view/link to file in repo:

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Project%20Risk%20Assessment%20Screenshot.JPG" width="1000"/>
</p>

---

<a name="unit-testing"></a>
### Unit Testing

Tests are written to test the functionality of the individual components and functions comprising the app.  As this is a Flask application, I create a TestBase class with the prerequisite three methods used in defining the test conditions: create_app(), setUp() and TearDown().  These are run sequentially around each unit test i.e. the database is setup, a given test is run, the database is torn down then on to the next test, rinse and repeat.  Essentially building a dummy database for the purposes of testing using sqlite (test.db) within which I instantiate some dummy data using for loops (adding to the Students and Houses tables).  

Tests are defined in test_app.py in the tests folder and all classes and their respective methods are run when pytest is run.  This should be repeatable when this repo is cloned down and the requirements (including pytest module) are installed using the requirements.txt file.

Ongoing testing is baked into the development process using a continuous integration pipeline (CIP) via Jenkins.

---

<a name="jenkins"></a>
### Jenkins and Automation

Jenkins is an automation server.  In this case I am using it to facilitate building, testing and deployment in a continuous process - in other words a pipeline for the app's ongoing integration and delivery.  I was able to run consecutive builds of the app using Jenkins as well as perform the unit testing I had prewritten via an execute shell script (see image below): 

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Execute%20Shell%20for%20Latest%20Build.JPG" width="700"/>
</p>

In the below images you can see a build history for the app and an image showing the most recent build.

Build History:

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/build%20history.JPG" width="700"/>
</p>

Successful build following the addition of further functionality and its corresponding unit tests:

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Build%20After%20Changes.JPG" width="700"/>
</p>

The two images encapsulate the idea of continous integration, whereby changes to the code are made between builds and the same tests (or perhaps additional ones too) are run to determine if the app is still functioning as intended and if it is still deliverable to users.  Ongoing development of the app is test driven.  Any changes are subjected to the same collection of tests such that a high standard of performance is maintained and future proofing is inbuilt.

---

<a name="test-analysis"></a>
### Test Analysis - what was tested and why - summary of overall results

Each route is tested, be it one that calls a function with a Post or Delete or be it simply an html page displaying database contents to the user.  When sent a GET request, routes ought to return a 200 status code response indicating the app is running correctly when a user follows said route.

Each class tests a different aspect of functionality.  For example the read class tests the responses for all the pages where data from the dummy database should be displayed - i.e. register, listhouses, liststudents.

In addition to checking status codes and interrogating response data, I have also included classes to test the contents of the data itself following HTTP requests and their respective responses.  By turning html into a string and decoding it one can determine that the change one has attempted to make has indeed been made and exists within the data itself rather than simply in the response (please see use of "assert" in the TestData class).

For example in the case of the edit functionality whereby a user wants to change a student's name or house or indeed change the name of a house one needs to test the route for the corresponding function (amend student or amend house).  If I supply a particular name in the form data does that name then appear in the actual db data following the post request?

Please see the comments within test_app.py which describe the purposes of each test class.

The overall coverage of the tests is shown in the below image (I have since added additional tests though the coverage remains the same).

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Project%20Coverage%20report.JPG" width="1000"/>
</p>

The 98% coverage total indicates that most routes and functionality of the app have been tested and are working as intended.  When the tests are run as part of a Jenkins build, a coverage report is then included in the console log for said build.  Below is a screen showing these results (albeit for a slighly different version where the coverage is marginally different):

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/Build%20running%20latest%20tests.JPG" width="700"/>
</p>

I have tried to test all available routes and data types - one can see which lines in routes.py have not been covered by the tests.  There are likely more use scenarios that aren't covered by testing but in terms of the basic core functionality I believe all aspects have been covered off here i.e. most of the different possible interactions a user might have.  It should be noted that users are unable to delete houses that have students due to that dependency - the app throws an error in this scenario.  This is something that would ideally be avoided even via a message along the lines of "unable to perform this action as this house currently has students registered to it".

---

<a name="front-end"></a>
### Front-End Design: Flask (HTML)

* The entry point or homepage is navigated to via the "/" url suffix or alternatively the /register url endpoint.  It provides a portal for new/existing students to register their attendance of a particular house.  The houses are accessible via a drop down menu and a user input box is available to accept a user's name.

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/project%20index.JPG" width="800"/>
</p>

* Once users input their name and house choice they are able to submit via the "sort me non-random hat" button.  Their records then appear on the left hand side of the page along with any other students currently registered and their respective houses. 

* I am using Bootstrap 3 for the Navbar.  The Navbar is coded into a base.html which can then be extended for the other pages via code blocks.

* There are various links in the Navbar.  The title and Entrol option bring the user back to the homepage/index.  The Add Houses link allows a user to enter a new house choice into the db which then becomes accessible in the drop down menu on the homepage.  The edit/delete students and edit/delete houses pages are accessible via links.  Those respective pages look as follows when there are some students already registered:

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/project%20edit%20students.JPG" width="800"/>
</p>

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/images/project%20edit%20houses.JPG" width="800"/>
</p>

Clicking on the appropriate button will either delete an entry or bring up a form to enter new information to update.

---

<a name="version-control"></a>
### Version Control: Git

I plan to use git branching to develop different features/components of my app.  Once I have a basic functionality working (app-setup) I will branch off when trying to tackle more complex components such as the update functionality via an HTML form.  This should be evidenced via my commit history.  Such an approach helps ensure the rest of the app retains its functionality whilst one individual element is being developed (although of course there may be dependencies) as it restricts the changes to one portion of the code.  I am also then able to confirm the code is working as best I can on whatever feature branch I am on before submitting a pull request, helping to ensure there is always a working version of the code in continuous delivery.  It mimics best practice in a professional environment where there'd be a dev branch and multiple developers working on respective branches.  Proposed merges are then peer reviewed and any conflicts resolved beforehand.  This keeps the codebase functional as a whole.  I'm trying to build the right habits. 

---

<a name="future-development"></a>
### Possible Future Development

* It would be ideal to add a login system and levels of permission for various aspects of functionality.  Students shouldn't be able to delete records other than their own for example. 
 
* I would also like to add a random sorting hat option or even a short questionnaire type form which would then assign users based on their answers.  More info could be added to new tables in the db such as student owl names, photos, classes etc. 

* Essentially a yearbook with an academic twist.  It could be a learning portal for Harry Potter enthusiasts.

* If this app were to continue with an Harry Potter theme in a commercial sense then permission/license would need to be sought out from the rights holders.  It might be simpler to develop the app fully with generic names or find a use outside of that franchise.

---

<a name="acknowledgements"></a>
### Acknowledgements

Thanks especially to Earl Gray for his expert tutelage and sticking with us!  A special mention also to Leon Robison for providing assistance when it was much needed.  Also to the rest of my cohort for their continued support and guidance :)

Also I'd like to thank J.K. Rowling for use of her house names and stories as inspiration for this app and would like to state this has strictly been for educational purposes and will not ever be put to commercial use.






 




