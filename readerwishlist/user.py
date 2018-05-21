"""
user.py

Accessing all users and performing updates for that user
endpoint - /users/<id>
"""
from readerwishlist.db import query_db, get_db
from flask import (g, request, session, url_for, jsonify)
from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256

class User(Resource):

	def get(self, user_id):
		""" retrieve all info for the current user
		"""
		user = query_db('SELECT id, firstname, lastname, email FROM user \
			WHERE id = ?', (user_id,), one=True)
		if user is None:
			return "User not found", 404

		response = jsonify(user)
		response.status_code = 200
		return response

	def put(self, user_id):
		""" update an existing user's firstname and lastname
			cannot change email or password information as of now
		"""
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

		if firstname is "" or lastname is "" or email is "" or password is "":
			return "Bad user data", 400

		user = query_db('SELECT password, email FROM user WHERE id = ?', (user_id,), one=True)

		if user is None:
			return "User not found", 404
		else:
			if pbkdf2_sha256.verify(password, user['password']) and \
				email == user['email']:

				query_db('UPDATE user SET firstname = ?, lastname = ? \
					WHERE id = ?', (firstname, lastname, user_id), commit=True)
				return "", 200
			else:
				return "Authentication failure", 401

	def delete(self, user_id):
		""" deletes the current user information and any connections
			associated with that user
		"""
		user = query_db('SELECT id from user where id = ?', (user_id,))
		if user is None:
			return "User not found", 404

		query_db('DELETE from book where userId = ?', (user_id,))
		query_db('DELETE from user where id = ?', (user_id,), commit=True)
		return "", 204
