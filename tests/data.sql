DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	firstname TEXT NOT NULL,
	lastname TEXT NOT NULL,
	password TEXT NOT NULL,
	email TEXT UNIQUE NOT NULL
);

CREATE TABLE book (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	author TEXT NOT NULL,
	isbn TEXT UNIQUE NOT NULL,
	publication_date TEXT NOT NULL,
	userId INTEGER,
	FOREIGN KEY(userId) REFERENCES user(id)
);

INSERT INTO user (firstname, lastname, password, email) VALUES ('Eloi', 'Wells', '$pbkdf2-sha256$10000$AcCYs1bqndM6B2Cs1bpXSg$aV8LAyZxZcoSo3KmiO9Q6Jfe5jmBEweoN5x5oIZmUnE', 'eloi@mutiny.com');
INSERT INTO user (firstname, lastname, password, email) VALUES ('Morlock', 'Herbert', '$pbkdf2-sha256$10000$qtUa47w3xrhXqlUKodS6Nw$kC6dUYuNdrNXsXfrmuH2pOukEmqS9YAKOG0ZfcxsEXg', 'morlock@westgroup.com');

INSERT INTO book (title, author, isbn, publication_date, userId) VALUES ('The Martian', 'Andy Weir', '978-0-8041-3902-1', 'Feb 11 2014', 1);
INSERT INTO book (title, author, isbn, publication_date, userId) VALUES ('The Cathedral and the Bazaar', 'Eric S. Raymond', '978-0-596-00108-7', 'Feb 1 2001', 1);
INSERT INTO book (title, author, isbn, publication_date, userId) VALUES ('Ready Player One', 'Ernest Cline', '978-0307887443', 'Jun 5, 2012', 2);
INSERT INTO book (title, author, isbn, publication_date, userId) VALUES ('American Gods', 'Neil Gaiman', '978-0062059888', 'Jun 21, 2011', 2);
INSERT INTO book (title, author, isbn, publication_date, userId) VALUES ('The Painted Veil', 'W. Somerset Maugham', '978-0307277770', 'Nov 14, 2006', 2);
