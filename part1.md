# Project 1, Part 1

* Assigned: 9/6
* Due: 9/27 10AM, digital copy
* 25% of overall Project 1 grade

In Part 1, you will propose a web application to build for the rest of Project 1.  You will design the entity-relationship diagram and schema of the database, and do some setup for Part 2.

These directions are long, but please read them carefully before you start.

**Note**: If you observe holidays that overlap with this part of the project, please email the instructor to arrange for alternative deadlines.

* [FAQs](#frequently-asked-questions)
* [Project overview: Read this carefully before starting](../../)
* [Staff Approval Meeting Signup](https://calendar.google.com/calendar/selfsched?sstoken=UUI4NUh4ZzQ0RURhfGRlZmF1bHR8MjYwM2U0MTZiNDU4YTFiNTI0OWQ4OTcwODFhYmZhMGI): Meet as a team to discuss the project with an IA in **CS TA room**, or with Prof. Wu in **MUDD 421**. We want to make sure the scope is appropriate. You should complete Step 1 before the meeting. 
<!--* CVN students still need to meet us for project 1 part 1, the local teammate can represent both of you. For teams that both students are remote, we will use Skype to meet. If you have a large time difference (e.g., singapore) then arrange so that the staff member knows.-->


# Overview 

This assignment consists of multiple steps.  At a high level, you will

1. Find teammate
1. Select an application, write a short proposal and construct the Entity-relationship diagram.
1. Meet with staff for approval and feedback
1. Revise proposal and E/R diagram, create SQL schema for the database.

If you're having trouble thinking of an application, look for a real dataset to design the application around.  Some possible suggestions could be local government datasets like [NYC Open Data](https://opendata.cityofnewyork.us/), [Columbia Libraries catalog](https://library.columbia.edu/bts/clio-data.html), [Bio datasets](https://github.com/OpenGene/awesome-bio-datasets), [Political datasets](https://fivethirtyeight.com/features/why-were-sharing-3-million-russian-troll-tweets/), [Earthquake datasets](https://earthquake.usgs.gov/data/data.php), etc.  There are many small shops, galleries, communities, that could benefit from a web applications too!


### You Will Submit:

You will upload your final proposal as a PDF to Gradescope.

**Required** Application Proposal

* Describe the general "domain" of your application, construct an Entity-Relationship
  diagram, **and map it to a relational schema using the mapping technique 
  that we will cover in class.**
* Pick an application with a schema that is relatively substantial, but not too large. 
  * E/R design should have ~5-10 entity sets and a ~5-10 relationship sets. 
    You will get a sense if your design is too simple or too complex as diagram it.
    Discuss this with a TA during your advising session if you are in doubt.
  * Try to make your application interesting, including a variety of different kinds of attribute 
    domains (e.g., strings, integers, etc.) and relationships with different key and 
    participation constraints.
* Include as many relevant constraints for your application from the 
  real world as possible in your E/R diagram.

<a name="contingency"></a> **Optional but strongly recommended: Contingency plan for two-person teams**:
  Since students may drop classes, and to prevent last-minute surprises, we suggest that you 
  write a "contingency plan" in case a team-mate drops the class  later in the semester. 

* Indicate how you will simplify the project for a single person to complete. 
* Revised ER design with roughly 3-7 entity sets and 3-7 relationship sets.
* If your teammate drops the class, you will  complete the contingency version instead of finding a new teammate.

**If you choose not to submit this plan when you submit Part 1 and your team-mate drops the class later, you will have to complete the original project. No exceptions will be made at that point.**



## Step 1: Prepare for meeting with course staff

1. Find a team-mate and indicate them when submitting Part 1.
1. Write an informal one-paragraph description of the application (less than 20 lines). Highlight interesting and challenging parts. The more concrete your written description, the more efficient and useful the meeting with the class staff will be. This paragraph should include:
    * A high-level description of the general domain of the application. 
    * Examples of entities and relationship sets, attributes and real-world constraints you will have.
    * What data you will use to populate your database, you can use real data or make up your own.
    * Provide details about how users will interact with the site, please describe the general "entities" that are involved, and what types of operations users can perform. For example, if your website is based on the Internet Movie Database, the user might find actors of a moview, read review, add it to watchlist and find similar movies, etc.
1. Write a short description of your contingency plan (see above).
1. Construct the E/R diagram for the application. You will go over it with the staff during the meeting.
 
 
## Step 2: Revise and complete Part 1
 
1. Meet with a TA or the instructor to ensure the design is appropriate and get feedback:
    * This 10-15 minute meeting is required.
    * We will have expanded office hours during that week.
    * At least one must attend.  It's much better if both attend.
    * Bring **two copies** of the written materials for yourself and the staff.
    * **It is a good idea to come earlier in the week.**  If you choose to come later and it is too crowded, then you will be unhappy.
1. After the meeting, modify the description and E/R diagram based on the feedback.
1. Map your E/R diagram into a relational schema in SQL, preserving the constraints.
1. Submit a digital copy of the following on the due date:
    1. Revised one-paragraph description of the application
    2. Revised Entity-relationship diagram
    3. **Resulting SQL schema**
    4. Revised contingency plan (optional)
1. Keep a copy of all these materials for yourselves, since you will need them for Parts 2 and 3 


# Grading

Your grade will be split as follows:

* (7pts) Meeting with class staff: If you come to the meeting prepared with your written description and E/R diagram, you can expect to get all points, even if you are asked to make changes or revisions to your proposal.
* (6pts) Quality of final one-paragraph description of your application: We will evaluate the overall quality of your final one-paragraph description of your application, including how thoroughly you incorporated any revisions suggested during your meeting with the staff.
* (6pts) Quality of E/R diagram: We will evaluate how well your E/R diagram models your proposed application, including how well you modeled any relevant real-world constraints.
* (6pts) Quality of your SQL schema: We will evaluate how well you mapped your E/R diagram, including constraints, into a SQL schema using the technique that we covered in class.


# Frequently-Asked Questions
<a name="faq"></a>

* I have an idea that requires that I work alone. Can I?
    * No, sorry. Please modify your project idea so that it becomes appropriate for a two-person team. Yes, being forced to work with others is sometimes painful, but I believe that some of the most valuable lessons you learn in University are not the course content.

* Can we have a team of 3, 4, or 12 students?
    * No, sorry. For fairness and to make it possible for us to grade them, the projects need to have similar size and scope.

* Can I use my favorite DBMS instead of PostgreSQL?
    * No, sorry.  We would like to be more flexible but don't have the staff to handle several diverse systems and platforms.

* Can I use Java (or something that's not Python) for Option 3?
    * No, sorry. Please see the answer to the previous question.
    
<!--* I'm a CVN student, is the IA meeting mandotory?
    * Yes, you still need to meet us for project 1 part 1. The local teammate can represent both of you, if both students are remote, we will use Skype to meet. -->
