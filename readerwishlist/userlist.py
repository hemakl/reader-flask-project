
"""
userlist.py

This file will take care of retrieving all the users currently in the
database or will add a new user to the DATABASE.
endpoint - /users

"""
from readerwishlist.db import query_db, get_db
from flask import (g, request, session, url_for, jsonify)
from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256

class UserList(Resource):

	def get(self):
		""" retrieve all users currently in the database """
		user = query_db('SELECT id, firstname, lastname, email FROM user')
		if user is None:
			return "Users not found", 404

		response = jsonify(user)
		response.status_code = 200
		return response

	def post(self):
		""" create a new user
		grab the arguments from the request using a parser """
		parser = reqparse.RequestParser()
		parser.add_argument("firstname")
		parser.add_argument("lastname")
		parser.add_argument("email")
		parser.add_argument("password")
		args = parser.parse_args()
		firstname = args["firstname"]
		lastname = args["lastname"]
		email = args["email"]
		password = args["password"]

		# verify the information being passed through the request
		if firstname is "" or lastname is "" or email is "" or password is "":
			return "Bad user data", 400

		user = query_db('SELECT email FROM user WHERE email == ?', (email,))

		if user is None:
			# encrypt the password before storing it in the db
			passhash = pbkdf2_sha256.encrypt(password, rounds=10000, salt_size=16)

			user_id = query_db('INSERT into user (firstname,lastname,email,password) \
				VALUES (?, ?, ?, ?)', (firstname, lastname, email, passhash), \
				commit=True)
			return user_id, 201
		else:
			return "User already exists", 400
