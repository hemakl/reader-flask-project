import sqlite3

import click
from flask import (current_app, g)
from flask.cli import with_appcontext

# return the values from db as dictionary for easy access
def make_dicts(cursor, row):
	return dict((cursor.description[idx][0], value)
			for idx, value in enumerate(row))

# establish connection to
def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types=sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = make_dicts

	return g.db

# close db connection
def close_db(e=None):
	db = g.pop('db',None)

	if db is not None:
		db.close()

# run the query to the database and return any values if there are any
def query_db(query, args=(), one=False, commit=False):
	cur = get_db().execute(query, args)
	if commit:
		get_db().commit()
		return cur.lastrowid
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else (rv if rv else None)


# initialize the db with the given schema file
def init_db():
	db = get_db()

	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
	# This will remove all existing tables and their corresponding data
	# and create new tables
	init_db()
	click.echo("Initializing the database.")

# complete the registration with the application
def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)
