"""
booklist.py

Adding or listing all books associated to one user
endpoint - /users/<id>/books
"""

from readerwishlist.db import query_db, get_db
from flask import (g, request, session, url_for, jsonify)
from flask_restful import Resource, reqparse


class BookList(Resource):

	def get(self, user_id):
		""" retrieves the wishlist for the given user
		"""
		user = query_db('SELECT u.id from user u where u.id = ?', (user_id,))
		if user is None:
			return "User not found", 404

		books = query_db('SELECT * FROM book WHERE userId = ? ORDER BY \
			publication_date DESC', (user_id,))

		if books is None:
			return "No books found in wishlist", 404
		else:
			response = jsonify(books)
			response.status_code = 200
			return response

	def post(self, user_id):
		""" creates or adds a new book to the given user's wishlist
		"""
		user = query_db('SELECT id from user where id = ?', (user_id,))
		if user is None:
			return "User not found", 404

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

		book = query_db('SELECT b.id, b.isbn FROM book b WHERE b.isbn == ?', (isbn,))

		if book is None:
			if title is "" or author is "" or isbn is "" or publication_date is "":
				return "Bad user data", 400

			book_id = query_db('INSERT into book (title,author,isbn,publication_date,userId) \
				VALUES (?, ?, ?, ?, ?)', (title, author, isbn, publication_date, user_id), \
				commit=True)
			return book_id, 201
		else:
			return "Book already exists", 400


	def delete(self, user_id):
		""" deletes all books associated with the given user
		"""
		user = query_db('SELECT id from user where id = ?', (user_id,))
		if user is None:
			return "User not found", 404

		query_db('DELETE from book where userId = ?', (user_id,), commit=True)
		return "", 204
