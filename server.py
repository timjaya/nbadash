#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

from passlib.hash import sha256_crypt
import os
from os import path
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, flash, session, abort, url_for

tmpl_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

app.secret_key = 'super secret key'


# XXX: The Database URI should be in the format of:
#
#     postgresql://USER:PASSWORD@<IP_OF_POSTGRE_SQL_SERVER>/<DB_NAME>
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@<IP_OF_POSTGRE_SQL_SERVER>/postgres"
#
# For your convenience, we already set it to the class database

# Use the DB credentials you received by e-mail
DB_USER = "hha2116"
DB_PASSWORD = "IfALD2z6Ga"

DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"

DATABASEURI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_SERVER+"/w4111"


#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)


# Here we create a test table and insert some values in it
# engine.execute("""DROP TABLE IF EXISTS test;""")
# engine.execute("""CREATE TABLE IF NOT EXISTS test (
#   id serial,
#   name text
# );""")
# engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")

@app.before_request
def before_request():
    """
    This function is run at the beginning of every web request 
    (every time you enter an address in the web browser).
    We use it to setup a database connection that can be used throughout the request

    The variable g is globally accessible
    """
    try:
        g.conn = engine.connect()
    except:
        print("uh oh, problem connecting to database")
        import traceback
        traceback.print_exc()
        g.conn = None


@app.teardown_request
def teardown_request(exception):
    """
    At the end of the web request, this makes sure to close the database connection.
    If you don't the database could run out of memory!
    """
    try:
        g.conn.close()
    except Exception as e:
        pass

#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
#
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
    """
    request is a special object that Flask provides to access web request information:

    request.method:   "GET" or "POST"
    request.form:     if the browser submitted a form, this contains the data in the form
    request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

    See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
    """
    return render_template("index.html")

##
# Example of adding new data to the database
# @app.route('/add', methods=['POST'])
# def add():
#   name = request.form['name']
#   print(name)
#   cmd = 'INSERT INTO test(name) VALUES (:name1), (:name2)';
#   g.conn.execute(text(cmd), name1 = name, name2 = name);
#   return redirect('/')
@app.route('/search-player')
def search_player():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    query = request.args.get('query')
    orderby = request.args.get('orderby')

    if query is None: 
        query = ''
    
    name = ('%' + query + '%').lower()
    cmd = 'SELECT p.pid, name, current_team, avg(points) as avg_points, avg(steals) as avg_steals, avg(blocks) as avg_blocks ' \
        'FROM Player_Plays g, Player p ' \
        'WHERE g.pid = p.pid AND LOWER(name) LIKE (:name) ' \
        'GROUP BY p.pid, name, current_team '
    
    if orderby is not None:
        cmd = cmd + 'ORDER BY ' + orderby + ' DESC LIMIT 20;'
    else:
        cmd = cmd + 'LIMIT 20;'

    cursor = g.conn.execute(text(cmd), name=name, orderby=orderby)
    result = []
    for item in cursor:
        result.append(item)
    cursor.close()

    context = dict(data=result, query=query)
    return render_template("search.html", **context)

"""
LOGIN PAGE
"""
@app.route('/login')
def login():
    if session.get('logged_in'):
        return redirect(url_for('search_player'))
    return render_template("login.html")

@app.route('/login-attempt', methods=["POST"])
def login_attempt():
    username = request.form['username']
    password = request.form['password']
    
    cmd = 'SELECT password ' \
        'FROM Users u ' \
        'WHERE u.uid = (:username);'

    cursor = g.conn.execute(text(cmd), username=username)
    result = [item for item in cursor]
    cursor.close()
    if not result: 
        flash('Invalid Credentials.')  
    elif len(result) > 1:
        flash('Duplicate Usernames. Contact Admin.')
    else:  
        verified = sha256_crypt.verify(password, result[0]['password'])
        if verified:
            session['logged_in'] = True
            session['username'] = username
        else:
            flash('Invalid Credentials.')    
    return redirect(url_for('search_player'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['username'] = None
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup/adduser', methods=['POST'])
def signup_add_user():
    username = request.form['username']
    password = sha256_crypt.encrypt(request.form['password'])
    email = request.form['email']
    
    # check first if username already exists
    cmd = 'SELECT uid ' \
        'FROM Users u ' \
        'WHERE uid = (:username);'
    cursor = g.conn.execute(text(cmd), username=username)
    result = [item for item in cursor]
    cursor.close()
    if result:
        flash('Username already taken.')
        return redirect(url_for('signup'))

    # check first if email already exists
    cmd = 'SELECT email ' \
        'FROM Users ' \
        'WHERE email = (:email);'
    cursor = g.conn.execute(text(cmd), email=email)
    result = [item for item in cursor]
    cursor.close()
    
    if result:
        flash('Email already taken.')
        return redirect(url_for('signup'))
    
    cmd = "INSERT INTO Users (uid, email, password)" \
          "VALUES ((:username), (:email), (:password));"
    cursor = g.conn.execute(text(cmd), username=username, email=email, password=password)
    cursor.close()
    return redirect(url_for('login'))

@app.route('/players/<pid>')
def players(pid):
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        cmd = 'SELECT name, birthdate, height, weight ' \
              'FROM Player ' \
              'WHERE pid = (:pid);'
        
        cursor = g.conn.execute(text(cmd), pid=pid)
        result = [item for item in cursor]
        cursor.close()

        context = dict(data=result)
        # TODO: need error handling if return two outputs

        return render_template('players.html', **context)

if __name__ == "__main__":
    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):
        """
        This function handles command line parameters.
        Run the server using

            python server.py

        Show the help text using

            python server.py --help

        """

        # reload templates when HTML changes
        extra_dirs = [os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'templates'), ]
        extra_files = extra_dirs[:]
        for extra_dir in extra_dirs:
            for dirname, dirs, files in os.walk(extra_dir):
                for filename in files:
                    filename = path.join(dirname, filename)
                    if path.isfile(filename):
                        extra_files.append(filename)

        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))

        app.run(host=HOST, port=PORT, debug=debug,
                threaded=threaded, extra_files=extra_files)

    run()

    #
    # Flask uses Jinja templates, which is an extension to HTML where you can
    # pass data to a template and dynamically generate HTML based on the data
    # (you can think of it as simple PHP)
    # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
    #
    # You can see an example template in templates/index.html
    #
    # context are the variables that are passed to the template.
    # for example, "data" key in the context variable defined below will be
    # accessible as a variable in index.html:
    #
    #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
    #     <div>{{data}}</div>
    #
    #     # creates a <div> tag for each element in data
    #     # will print:
    #     #
    #     #   <div>grace hopper</div>
    #     #   <div>alan turing</div>
    #     #   <div>ada lovelace</div>
    #     #
    #     {% for n in data %}
    #     <div>{{n}}</div>
    #     {% endfor %}
    #

    # if not session.get('logged_in'):
    #     return render_template('login.html')
    # else:
    #     # DEBUG: this is debugging code to see what request looks like
    #     print(request.args)

    #     #
    #     # example of a database query
    #     #
    #     cursor = g.conn.execute("SELECT name FROM test")
    #     names = []
    #     for result in cursor:
    #         # can also be accessed using result[0]
    #         names.append(result['name'])
    #     cursor.close()
    #     context = dict(data=names)

    #     #
    #     # render_template looks in the templates/ folder for files.
    #     # for example, the below file reads template/index.html
    #     #



# @app.route('/api/search-player', methods=['POST'])
# def api_search_player():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         name = ('%' + request.form['name'] + '%').lower()
#         cmd = 'SELECT p.pid, name, current_team, avg(points) as avg_points, avg(steals) as avg_steals, avg(blocks) as avg_blocks ' \
#               'FROM Player_Plays g, Player p ' \
#               'WHERE g.pid = p.pid AND LOWER(name) LIKE (:name) ' \
#               'GROUP BY p.pid, name, current_team '

#         cursor = g.conn.execute(text(cmd), name=name)
#         result = []
#         for item in cursor:
#             result.append(item)
#         cursor.close()

#         context = dict(data=result)
#         return render_template("search.html", **context)

