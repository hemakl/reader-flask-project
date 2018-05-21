import os

from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from readerwishlist.book import Book
from readerwishlist.booklist import BookList
from readerwishlist.user import User
from readerwishlist.userlist import UserList


# configure the app
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True, static_url_path='')
	api = Api(app)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'readerwishlist'),
	)

	# load instance config, if one exists, depending on testing or not
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# initialize the db app
	from . import db
	db.init_app(app)

	# static file to display the http status codes used
	@app.route("/")
	def root():
		return app.send_static_file("index.html")
	#def hello_world():
	#	return "Hello, World!"

	# routes setup for each endpoint
	api.add_resource(User, "/users/<int:user_id>")
	api.add_resource(UserList, "/users")
	api.add_resource(BookList, "/users/<int:user_id>/books")
	api.add_resource(Book, "/users/<int:user_id>/books/<int:book_id>")

	return app
