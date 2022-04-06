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
updating the backlog, sprint backlog and completed sprint at the end of each day.  I will demonstrate I am doing this via numbered screenshots 
of my Trello board which I will include in this repo, along with any accompanying documents which I will include links to below.

### Day 1
I set up a new VM on GCP and this GitHub repo.  Installed Jenkins on my VM.  Cloned this repo down.  Got a very basic app running with CRUD functionality based on a previous exercise.
Signed up for Trello - wrote day 1 Agile Sprint Board - took a screenshot.
Decided to simplify my project to something that was one to many - came up with this Harry Potter Houses idea.
Devised user stories.
Signed up for drawio and did a basic sketch of the table relationships between students, houses and years (should I have time to include student year).

### Day 2
Researched further re: MoSCoW and refined my user stories and the MVP requirements of the task such that they were aligned with the must haves.  I decided to consider the examiner user story as a key one - after all the purpose of this project is to assess our progress and to be a quality gate therefore that is the most important user story - a collection of must haves!  This isn't intended at this stage to be an app that is used widely.

![alt text](https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/Hogwarts%20Houses%20ERD.drawio.png)

https://github.com/Harry84/DevOps-Core-Fundamental-Project/blob/main/Hogwarts%20Houses%20ERD.drawio.png

