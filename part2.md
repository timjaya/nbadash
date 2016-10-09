# Project 1, Part 2

* Assigned: 10/3
* Due: 10/17 10:00AM Electronically
* Value: 25% of Project 1 grade


In this part of the project, you will revise your design based on the staff's feedback on [part 1](./part1.md). You will implement the database tables (including all constraints), populate the database, and write some queries.

* [Project overview](./README.md)
* If your teammate has dropped the class, [see the contingency plan](./part1.md#contingency)
* For any questions about collaboration, [see the Syllabus](http://github.com/w4111/syllabus#cheating)
* If there are questions of general interest, please post to Piazza.



# Logistics

Project mentor

* The TA that graded your part 1 will be your project mentor for the rest of your project -- 
  this is likely the TA that you discussed part 1 with.  He or she will be your main contact for 
  the project, though the rest of the staff are of course available for questions or concerns.


<a name="GCP"></a>
Google Cloud Platform

* Go to [https://www.cs.columbia.edu/auth/cloud](https://www.cs.columbia.edu/auth/cloud) and fill out your name to create a Google Cloud account. You will receive an invitation email from no-reply@cloud.cs.columbia.edu, go to [https://console.cloud.google.com](https://console.cloud.google.com) and log in with cloud.cs account and the temporary password. You will be prompted to change your password.
* We have messaged you your coupon code for Google Cloud through Courseworks. **Make sure you are logged in with your cloud.cs account**, sign out from other Google accounts if necessary, go to [https://console.cloud.google.com/education](https://console.cloud.google.com/education), enter your code in the “coupon code” box, then click accept and continue. 


Computing and Databases

* In the upper left Project dropdown, click create project and name it W4111. Then create a new VM following [steps to set up server](./Steps_to_setup_server.pdf) on Google Cloud Platform. You need to associate a billing acount with the project, use the one that is created when your coupon code is redeemed. You can then use this VM to complete the assignment and all future assignments that require a VM.
* You are welcome to setup PostgreSQL on your VM, see instructions at [https://cloud.google.com/solutions/set-up-postgres](https://cloud.google.com/solutions/set-up-postgres). Or you can use the databases that the staff is running for you.



# Procedures

Preliminaries

1. Pick up your graded Part 1 starting on **10/10**, and revise your design based on its feedback.
  * You will be graded based on how well you addressed the project mentor's comments. 
    In general, listen to your project mentor's suggestions.
2. Familiarize yourself with the [PostgreSQL documentation](http://www.postgresql.org/docs/9.3/interactive/index.html)!
   We will use PostgreSQL 9.3 (the minor version .3 doesn't matter so much).


Make the database

1. Connect to your database (only one team member needs to do this database part)
  * Navigate to your instance in the Cloud Platform Console, click the ssh button that appears next to your instance, a command line window will pop up
  * Install psql, two steps

          sudo apt-get update
          sudo apt-get -y install postgresql postgresql-client postgresql-contrib

  * After the installation is completed, connect to our postgres database using `psql`command

          psql -U <your uni> postgres -h 104.196.175.120

  * It will ask for your password, which is included in the Courseworks message we sent. If you didn't get the message, post a private question on Piazza. You may play with Postgres a little bit before the graded project 1 part 1 is returned to you.
  * If the database cannot handle the number of connections, we may create a second database server (we will let you know!)

1. Create the SQL tables based on your revised schema.
  * Include all key, type constraints
  * The PostgreSQL documentation for [CREATE TABLE](http://www.postgresql.org/docs/9.3/static/sql-createtable.html)
    and [data types](http://www.postgresql.org/docs/9.3/static/datatype.html) may help

1. Create the CHECK constraints that you need to express the rest of your real-world constraints.
  * Note: PostgreSQL's CHECK constraints are limited ([see the documentation](http://www.postgresql.org/docs/9.4/static/ddl-constraints.html)), so do what you can.
  * Note: PostgreSQL doesn't support CREATE ASSERTION statements. but does support triggers.
    However, you are not required to implement constraints that require triggers

Populate the tables

1. Insert at least 10 realistic/real tuples into each table in your database.
  * This should be based on your description in part 1

Run some queries

1. Run 3 interesting queries.
   The three queries, together, should include multi-table joins, WHERE clauses, and aggregation (e.g. COUNT, SUM, MIN, etc). Each
   query does not need to include all of those SQL features.



# Submission
<a name="submit"></a>

Since you created the database on the course database machine, we have access to your database and populated tables, so you are almost done!

Go to [the google docs form](https://docs.google.com/a/columbia.edu/forms/d/e/1FAIpQLSedv3T4Nnq9rN_2iqVO6NrQLXBWGricD-3XRd4Bg8xDy85Ijw/viewform) and fill it out. You can edit your submission until the due date (be careful, since if you submit afterwards it will be counted as late). We will use the google docs submission timestamp.

Finally, turn in the _graded_ ER diagram from part 1 at the beginning of class (this is part of the assignment, so late days will be in effect).



# Grading 
<a name="grading"></a>

Grading depends on the following:

* how well you incorporated your mentor's feedback (important)
* Quality of the SQL schema and implementation:  how well it conforms with the ER diagram and constraints
* Your SQL statements: are they reasonable application queries and do they use the SQL features as requested?
* Quality of the data: is it realistic?  

