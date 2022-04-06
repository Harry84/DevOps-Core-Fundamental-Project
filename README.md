# DevOps-Core-Fundamental-Project: 
## Harry Potter Sorting Hat
### Intro

This is a basic web app intended to allow users (aka Hogwarts Students) to register their attendance of one of the four houses at Hogwarts.

As an MVP, two tables will be included in a relational db - one for houses and a second for student names - a one to many relationship - there are many students but each may only belong to one of the four houses.  Users enter their name via a form and select a house to join.
Their name is then appended to a list of students within that house which they can then see displayed on a roster/home page along with the names of students in the other houses.

Ideally I will try to include a random element to assign houses (sorting hat) to prospective students and potentially will extend to include another table, student 
years.

### Approach

I aim to use an agile approach in carrying out this project.  I will interpret user stories corresponding to my understanding of the MVP
and how it applies here.  On a daily basis, I will then set tasks to enable these user stories.  Given the short 
turnaround time of the project I will view each day as its own sprint and try to allocate tasks to my Trello board in the morning, as well 
updating the backlog, sprint backlog and completed sprint at the end of each day.

### Day 1
* Decided to use Trello from the get go to help with planning and prioritisation.  Each day is treated as a sprint with its own backlog.  At the end of the day I move the completed task cards over to the completed sprint section of the board on the right hand side (see image below).

![alt text](https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/Trello%20Board%20Day1.JPG)


* This was a setup and planning day mainly - you can see roughly what I achieved in the completed tasks on the Trello Board.
* Decided to simplify my project to something that was one to many - came up with this Harry Potter Houses idea.
* Signed up for drawio and did a basic sketch of the table relationships between students, houses and years (should I have time to include student year) - aka Entity Relationship Diagram (see below):

![alt text](https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/Hogwarts%20Houses%20ERD.drawio.png)

* Devised user stories - I decided to consider the examiner user story as a key one - after all the purpose of this project is to assess our progress and to be a quality gate therefore that is the most important user story - a collection of must haves!  This isn't intended at this stage to be an app that is used widely.

### User Stories

_Must Haves:_

Must meet MVP definition: a project that satisfies the minimum passing requirements of the assignment

As the examiner I want to see the following evidenced in the project in order that it may pass:


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

Ages of students
Last names of students
Sorting hat option for random house assignment
Some sort of sorting hat gif?
Another table


_Won't have:_

A good looking front end
Any CSS or JS
Buttons/interactivity for the user
login system

### Table relationship

The two tables are Students and Houses - they share a one to many relationship in that Houses may have many students but each student may only be in one house.  This is shown symbolically via the line linking house_id within the Student table to house_id in the Houses table.   Each house can have many students, therefore the connecting line branches where it meets the Houses table.  Each student can only have one house, denoted by the single branch where the line meets the Students table.  Each student record has a house_id corresponding to the id of that student's house.  House_id is the primary key in the Houses table and the foreign key in the Students table.

### Database

I have instatiated an SQL server on the GCP.  I am connecting to my database schema via Workbench.

### CRUD Functionality

Using Flask and SQLAlchemy, I instantiate a db object using:

db = SQLAlchemy(app) in the init file.

I define the classes I want to use in models.py.  Each class has attributes which form the columns of the db.  New entities are then instantiated in python via providing arguments to these classes.  These are only currently objects in Python.  In order to add them to the database I add and commit them. Please see routes.py for examples of the following:

* Create:
    Students and Houses are created
* Read:
    Student and house table entries are read
* Update:
    Student entries are updated (routes.py line 67)
* Delete:
    Student entries are deleted (routes.py line 38)




 




