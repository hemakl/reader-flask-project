"""
book.py

Gets all book information associated to a single user
endpoint - /users/<id>/books/<book-id>
"""
from readerwishlist.db import query_db, get_db
from flask import (g, request, session, url_for, jsonify)
from flask_restful import Resource, reqparse


class Book(Resource):

	def get(self, user_id, book_id):
		""" gets the associated book for the given user
		"""
		book = query_db('SELECT * FROM book WHERE userId = ? and id = ?', \
			(user_id, book_id,), one=True)

		if book is None:
			return "Resource not found", 404

		response = jsonify(book)
		response.status_code = 200
		return response

	def put(self, user_id, book_id):
		""" updates the information pertaining to a single book
			cannot change the isbn information
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("title")
		parser.add_argument("author")
		parser.add_argument("isbn")
		parser.add_argument("publication_date")
		args = parser.parse_args()
		title = args["title"]
		author = args["author"]
		isbn = args["isbn"]
		publication_date = args["publication_date"]

		if title is "" or author is "" or isbn is "" or publication_date is "":
			return "Bad user data", 400

		book = query_db('SELECT * FROM book WHERE userId = ? and id = ?', \
			(user_id, book_id,), one=True)
		if book is None:
			return "Resource not found", 404

		if isbn == book['isbn']:
			query_db('UPDATE book SET title = ?, author = ?, publication_date = ? \
				WHERE id = ?', (title, author, publication_date, book_id), commit=True)
			return "", 200
		else:
			return "Bad user data", 400


	def delete(self, user_id, book_id):
		""" deletes the book associated to the given user
		"""
		user_book = query_db('SELECT * FROM book WHERE userId = ? and id = ?', \
			(user_id, book_id,), one=True)
		if user_book is None:
			return "Resource not found", 404

		query_db('DELETE FROM book WHERE id = ?', (book_id,), commit=True)
		return "", 204
