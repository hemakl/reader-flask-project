
The project was to create a RESTful API in Python3 to manage a user's reading
wish list. This project's API is documented in the homepage at http://localhost:5000/
once the project is running. You can optionally find this file at
reader-flask-project/readerwishlist/static/index.html (it is recommended to
view this file with a browser). This has been developed and tested on Windows only. 

Tools Used:
	Python3.6.3 - language of API
	flask_restful 1.0.2 - web framework
	passlib1.7.1 - used for password hashing
	SQLite3 - for database storage
	pytest - testing framework

SQLite3 was chosen as the database backend as it requires minimum time to set up and is
also extremely portable. It also works with a variety of web frameworks and has a lot of
support.
Flask-RESTful was picked as it's a micro-framework and would work well for RESTful
routing and gives you a development server. The downfall is that it works only in a development
environment. When deploying to production, a different service, like Waitress, should be chosen.
If deploying to production, this should be in SSL mode. In which case, OoenSSL will need to
be installed.

passlib was chosen for sha256 encryption of the user password.

This project is delivered with the top level directory being reader-flask-project.
To run this project, launch it inside a virtual environment to keep all python
dependencies from interfering with your normal dev environment. The following
procedure will launch the virtual environment. You will then install packages only
into that sandboxed environment, setup the proper variables to run the project in
the flask development application server, and launch the project.

1) download or clone repo from git (link in email)
2) 'cd' into reader-flask-project
3) create a virtual env by running 
	python -m venv booklist_env
4) run the batch or shell script at booklist_env\Scripts\activate to move into
   the virtual environment
5) once your prompt changes, 
	run 'pip install flask-restful',
   	run 'pip install passlib', 
   	run 'pip install pytest'
6) set FLASK_ENV to development (i.e. set FLASK_ENV=development)
7) set FLASK_APP to readerwishlist (i.e. set FLASK_APP=readerwishlist)
8) run 'flask init-db' (creates the tables and associated columns)
9) run 'flask run' (this starts the flask application running the project)
10) the app is now running on 127.0.0.1:5000

Run Manual Test Execution Script
---------------------------------
11) ./manual_test.sh (will execute a series of commands using the API)
**Caveat - The Test script file consists of happy path tests only. Comprehensive tests that
exercise all status codes are located in the SWIT tests and should be run using pytest

Optionally to execute Integration tests
---------------------------------------
12) 'cd' into 'tests' directory
13) type 'pytest' (this will run all the tests, optionally use -v option)

To exit the virtual environment
-------------------------------
14) 'cd' back into reader-flask-project
15) run the batch or shell script at booklist_env\Scripts\deactivate (your
    prompt will go back to normal)


Enhancements:
--------------
For the immediate future, I can think of two enchancements to make.
1) I'm not currently using an ORM like SQLAlchemy. I would add this to further decouple
the software between code and database. This would also allow the use of other databases
than just SQLite3.
2) For production deployment, I would run Flask within a Python WSGI server, such as Waitress.

References:
------------
http://flask.pocoo.org
