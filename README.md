## Index
[Brief](#brief)
   * [My Solution](#mysolution)
   
[ERD and Diagrams](#erdanddiagrams)
   * [Initial ERD](#erd)
   * [Final ERD](#FinalErd)
   * [Risk Assessment](#riskassess)
   * [Risk Assessment Table](#risktable)
   * [User Stories](#userstories)

[Sprints & Planning](#spr1)
   * [Trello Board Sprint 1.0](#spr1)
   * [Trello Board Sprint 2.0](#spr2)
   * [Trello Board Sprint 2.1 Continued...](#sprF)
   * [Trello Board Completion Stage](#sprFF)
	
[Testing Methadology](#testingmethod)
   * [Generated Report](#testingreport)
     
[My Deployment Method](#deploymentmethod)
   * [What I used](#techused)

[Visual Representation of my Solution](#visrep)

[Retrospective](#improve)

[Authors](#authorsinv)

<a name="brief"></a>
## The Product Brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

<a name="mysolution"></a>
### Solution

I created a blogging site using Flask and Bootstrap for Front-End and Python, Jinja and SQL for the Back-End. The website is for users to voice their opinion on matters online without the worry of being judged. Users also have access to see the posts written by others on the site but are only able to edit and delete their own work. 

<a name="erdanddiagrams"></a>
## ERD and Diagrams

<a name="erd"></a>
### Initial Entity Relationship Diagrams
![Initial ERD](/images/olderd.PNG)

My initial idea was to make a site for users to come and plan their outfits. But after pitching my idea to my trainer (Syed) and thorough research, I realised it would be difficult to get the user to upload images onto the site as that would require extra effort from the user.

As I wanted to keep my idea simple and user friendly, I decided to build a blog instead. The relationship between the user to post is 1 to Many as one user can create many posts. As I required two tables and user isn't considered one, I added a tag table, which had a 1 to Many relationship with the posts. As for each post, many tags can be added.  

<a name="FinalErd"></a>
### Final Entity Relationship Diagrams
![Final ERD](/images/newerd.PNG)

<a name="riskassess"></a>
## Risk Assessment
<a name="risktable"></a>
## Risk Assessment Table
![Risk Assessment Table](/images/riskass1.PNG)
![Risk Assessment Table Part 2](/images/riskass2.PNG)

# Kanban  / Requirements / Product Backlog
As seen below I have created a priority list where all the requirements of the project are listed, I used a colour labelling method On Trello to make sure that each requirement had its own importance category.

![Kanban](/images/productbacklog.png) ![Labels](/images/keyfortrello1.png)

<a name="userstories"></a>
## User Stories (Users and Developers)
The user stories were also done in trello to be an indication to me of what I want to aim for and provide to the user. It improved my planning and encouraged me to stay on the right path without drifting into complexity. In addition to the image of my user stories, I attached the key for my sprints.  
![UserStories](/images/userstories.png) ![Labels](/images/keyforuserstory.PNG)

<a name="spr1"></a>
## Trello Board (Sprint 1)
![Trello Image](/images/sprintttt1.PNG)

<a name="spr2"></a>
## Trello Board (Sprint 2)
(insert sprint2 and how it followed from sprint1) 
![Sprint 2 Image](/images/spint2.PNG)

<a name="sprF"></a>
## Trello Board (Sprint 3)
Most of the project requirements have been fullfilled at this point and the final touches are being made, as you can see the items that needed actioning have been moved to the done stage and the few optional requirements are being finalised.
![Sprint 3](/images/sprint3.PNG)

## Trello Board (Sprint 4)
![Sprint 4](/images/sprint4.PNG)

<a name="sprFF"></a>
## Completion
(insert info about sprint3)
![Completion](/images/sprint4.PNG)

<a name="techused"></a>
### List of Technologies Used

* MySQL for Application Database
* Python - Coding in Flask
* Flask - Framework 
* Jenkins - CI Server
* Testing - Pytest
* [Github Project](https://github.com/thenu97/SFIA-PROJECT-QA) - Version Control System
* [Trello Board](https://trello.com/b/2j1mrZib/project-blog) - Project Tracking Board
* Google Cloud Platform Services (MySQL DB, Compute Engine, firewall)

<a name="testingmethod"></a>
## Testing Methodology
I decided to use pytest to run my tests, mostly checking database and url is functioning correctly. I automated testing and deployment using Jenkins. I made sure the test was done first before the application was deployed as a service. 

<a name="testingreport"></a>
### Testing Report (Pytest Generated HTML)
Below is the HTML Coverage Report that was generated using the command "coverage html" on VSCode. 
![HTML Coverage Report](/images/htmlcoverage1.png)
![HTML Coverage Report](/images/htmlcoverage2.png)

### Testing Report (Generated after automated Jenkins Test)
Here is the coverage report which was generated on Jenkins after the automated testing took place. 
![Jenkins Coverage Report](/images/testing1.PNG)

<a name="deploymentmethod"></a>
## Deployment
![Deployment Pipeline](/images/pipeline.PNG)
The Deployment pipeline for this Flask application was done using Git/Github for version control and automating that process using
webhooks with Jenkins, the process would then go into automatically triggering the testing phase which I did using Pytest on a VM running Jenkins, after the tests Jenkins will be triggered into the build process - where if the testing was successful, Jenkins will then build and deploy the app as a service.

<a name="visrep"></a>
### Front End Visual Representation of my Solution

### Homepage before login
![HomePage](/images/homebeforelogin.png)

### Homepage after login
![HomePage](/images/homeafterlogin.png)

### View Post (Clicked into)
![Advert View](/images/viewpost.png)

### Abouts Page
![Abouts Page](/images/about.png)

### Login Page
![Login Page](/images/login.png)

### Register Page
![Register Page](/images/register.png)

### User Registered!
![Register new user](/images/regsuccess.png)

### User Logged in
![User Logged In](/images/userlogging.png)

### Viewing User created Ad (Users can only edit and update their own ads)
![User Ad view](/images/editdelete.png)

### Create Adverts Page
![Create Ad Page](/images/createpost.png)

### Create Tag
![Create Tag](/images/addtag.png)

### Deleted Account
![Deleted Acc](/images/afteraccdelete.png)

<a name="evaluation"></a>
## Retrospect

(enter self reflection)


<a name="authorsinv"></a>
## Authors
Thenuja Viknarajah

