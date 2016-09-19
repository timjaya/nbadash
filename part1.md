# Project 1, Part 1

* Assigned: 9/14
* Due: 10/3 2:40PM in class, hard copy
* worth 25% of overall Project 1 grade

In Part 1, you will propose an interesting web application of your choosing, that will be the basis of the rest of Project 1.  You will design the entity-relationship diagram and schema of the database, and do some setup for Part 2.

These directions are long, but please read them carefully before you start.

**Note**: If you observe holidays that overlap with this part of the project, please email the instructor to arrange for alternative deadlines.

* [FAQs](#frequently-asked-questions)
* [Project overview: Read this carefully before starting](http://github.com/w4111/project1)
* [IA Meeting Signup Link](https://calendar.google.com/calendar/selfsched?sstoken=UUk5TGJVNWlLbUZGfGRlZmF1bHR8ODVlZDM5MTAxMTA4M2FmMjZkNWIzMzZiYmNmMDUxNzc): Meet as a team to discuss the project with an IA in **CS TA room**, or with Prof. Wu in **MUDD 421**. We want to make sure the scope is appropriate. Please make sure you have completed Step 1 below before your meeting. 
* CVN students still need to meet us for project 1 part 1, the local teammate can represent both of you. For teams that both students are remote, we will use Skype to meet. If you have a large time difference (e.g., singapore) then arrange so that the staff member knows.


# Overview 

This assignment consists of multiple steps.  At a high level, you will

1. Find a team mate -- go make new friends! (Or [post on Piazza](https://piazza.com/class/irvic0xfdqk3p6?cid=5))

1. Select an application, write a short proposal and construct the Entity-relationship diagram.

1. Meet with a course staff member as a team to get feedback on your proposal: [Signup Link](https://calendar.google.com/calendar/selfsched?sstoken=UUk5TGJVNWlLbUZGfGRlZmF1bHR8ODVlZDM5MTAxMTA4M2FmMjZkNWIzMzZiYmNmMDUxNzc)

1. Revise your proposal and E/R diagram, create SQL schema for the database.


If you're having trouble thinking of an application, take a look at pretty much any web site. They all have a similar themes and can be reduced to an appropriate scope for the project. For example, social networks (e.g., instagram, reddit, twitter), e-commerce (e.g., overstock, etsy, amazon), or content sites (e.g. The New York Times, Yahoo Finance) can all work. For example, shopping websites usually have products, users, orders, shopping carts etc.

You will ultimately submit the following as hard-copies:

1. **Required** Application Proposal

  * Describe the general "domain" of your application, construct an Entity-Relationship
  diagram, and map it to a relational schema using the mapping technique 
  that we will cover in class. 

  * Pick an application with a schema that is relatively substantial, but not too large. 
    * E/R design should have ~5-10 entity sets and a ~5-10 relationship sets. 
      You will get a sense if your design is too simple or too complex as diagram it.
      Discuss this with a TA during your advising session if you are in doubt.

    * Try to make your application interesting, including a variety of different kinds of attribute 
      domains (e.g., strings, integers, etc.) and relationships with different key and 
      participation constraints.

  * Include as many relevant constraints for your application from the 
    real world as possible in your E/R diagram.

1. <a name="contingency"></a> **Optional but strongly recommended: Contingency plan for two-person teams**:
  Since students may drop classes, and to prevent last-minute surprises, we suggest that you 
  write a "contingency plan" in case a team-mate drops the class  later in the semester. 

  * The contingency plan should indicate how you will make the project simpler, so that it is appropriate for a single person to complete. 

  * As general guidelines, your ER design for a one-person project should have around 3-7 
    entity sets and 3-7 relationship sets.

  * If your team-mate drops the class, rather than finding a new team-mate,
    you will complete the "downgraded" version of your original project. 

  * **If you choose not to submit this plan when you submit Part 1 and your team-mate drops the class later, you will have to complete the original project. No exceptions will be made at that point.**



## Step 1: Prepare for meeting with course staff

1. Find a team-mate. There's no need to notify us about your team. You will simply indicate who your team-mate is when you submit Part 1.

1. Decide on an application for your project and write an informal one-paragraph description of the application (less than 20 lines). Highlight interesting and challenging parts. The more concrete your written description, the more efficient and useful the meeting with the class staff will be. This paragraph should include:

  1. A high-level description of the general domain of the application. 

  1. Examples of entities and relationship sets, attributes and real-world constraints you will have.

  1. What data you will use to populate your database, you can use real data or make up your own.

  1. Provide details about how users will interact with the site, please describe the general "entities" that are involved, and what types of operations users can perform. For example, if your website is based on the Internet Movie Database, the user might find actors of a moview, read review, add it to watchlist and find similar movies, etc.

  1. Write a short description of your contingency plan (see above).

1. Construct the E/R diagram as designed for the database of your application. This does not need to be final, but will make your meeting with the staff substantially better and is strongly encouraged.
 
 
# Step 2: Revise and complete Part 1
 
1. Meet with a TA or the instructor during the week of September 21st-28th to discuss your design and make sure that it is appropriate (i.e., challenging enough, but not unrealistically so). 
    * This 10-15 minute meeting is required.
    * We will have expanded office hours during that week.
    * It is better if both team members can attend, but it is acceptable if only one can make it.
    * Bring two copies of the written materials for yourself and the staff.
    * **It is a good idea to come earlier in the week.**  If you choose to come later and it is too crowded, then you will be unhappy.

1. After a TA or the instructor has approved your proposal:
    * Modify the description and E/R diagram based on the feedback.
    
1. Map your E/R diagram into a relational schema in SQL, preserving the constraints.

1. Submit a hard copy of the following on the due date:
    1. Revised one-paragraph description of the application
    2. Revised Entity-relationship diagram
    3. Resulting SQL schema
    4. Revised contingency plan (optional)
 
1. Keep a copy of all these materials for yourselves, since you will need them for Parts 2 and 3 of the project.


# Grading

Your grade will be split as follows:

* Meeting with class staff: 7 points.

  * If you come to the meeting prepared with your written description and E/R diagram, you can expect to get all points, even if you are asked to make changes or revisions to your proposal.

* Quality of final one-paragraph description of your application: 6 points.

   * We will evaluate the overall quality of your final hard-copy one-paragraph description of your application, including how thoroughly you incorporated any revisions suggested during your meeting with the staff.

* Quality of E/R diagram: 6 points.

    * We will evaluate how well your E/R diagram models your proposed application, including how well you modeled any relevant real-world constraints.

* Quality of your SQL schema: 6 points.

    * We will evaluate how well you mapped your E/R diagram, including constraints, into a SQL schema using the technique that we covered in class.


# Frequently-Asked Questions
<a name="faq"></a>

* I have an idea that requires that I work alone. Can I?
    * No, sorry. Please modify your project idea so that it becomes appropriate for a two-person team. Yes, being forced to work with others is sometimes painful, but I believe that some of the most valuable lessons you learn in University are not the course content.

* Can we have a team of 3, 4, or 12 students?
    * No, sorry. For fairness and to make it possible for us to grade them, the projects need to have similar size and scope.

* Can I use my favorite DBMS instead of PostgreSQL?
    * No, sorry.  We would like to be more flexible but don't have the staff to handle several diverse systems and platforms.

* Can I use Ada (or something that's not Python) for Option 3?
    * No, sorry. Please see the answer to the previous question.
    
* I'm a CVN student, is the IA meeting mandotory?
    * Yes, you still need to meet us for project 1 part 1. The local teammate can represent both of you, if both students are remote, we will use Skype to meet. 
