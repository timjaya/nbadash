Install some software packages that we will need, using the Ubuntu package management tool apt-get. To install a package, type:

`sudo apt-get install <packagename1 packagename2 ...>`

Use this command to install the following packages:

* postgresql
* postgresql-server-dev-9.5
* python-virtualenv
* python-dev
* python-pip


e.g.,


`sudo apt-get install postgresql postgresql-server-dev-9.5 python-virtualenv python-dev python-pip`

# Set Up Python

Python, which you will use for Part 3 of the project, uses its own package manager to install/update/remove packages. In general, the following installs python packages:

``` python 
pip install <packagename>
```

Typically the package manager will require sudo and install the packages in a global folder that affects everyone using your machine. This is bad practice because different Python applications may use different versions of packages and it's easy to step on each other's toes.

We will use virtualenv to create virtual environments that contain their own copies of python and packages. When we work in a virtual environment, pip will install packages local to the environment rather than globally. If you are interested, you can read a detailed tutorial. We already installed the virtualenv command with apt-get above.

To set up your environment:

* Install some helper commands from the virtualenvwrapper package (this is the one time you should install globally):

	`sudo pip install virtualenvwrapper`

* Load the wrapper commands in the current shell:

	`source /usr/local/bin/virtualenvwrapper.sh`

* To make sure this takes effect each time you log in, add that command to the end of your ~/.bashrc file, either using an editor (like nano ~/.bashrc) or running the following:

	`echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc`

* Create a new environment (this will create a folder test/ in ~/.virtualenvs/):

	`mkvirtualenv test`

* Switch (activate) an environment by using workon: 

	`workon test`

* Switch out of an environment:

	`deactivate`


Now let's install a set of useful packages into your environment:

1. Activate your environment, as you did above

2. Install the following packages using pip (see above)

	* flask
	* psycopg2
	* sqlalchemy
	* click

  e.g.,

  `pip install flask psycopg2 sqlalchemy click`

3. Deactivate (and we are done!)
