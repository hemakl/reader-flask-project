import pytest

''' test FAILURE to add new book for unknown user '''
def test_add_book_user_not_found(client):
    response = client.post(
        '/users/7/books',
        data={'title':'Station Eleven', 'author':'Emily St. John Mandel', 'isbn':'978-0-8041-7244-8', 'publication_date':'Jun 2, 2015'}
    )
    assert response.status_code == 404

''' test FAILURE to add an existing book for known user '''
def test_add_book_book_exists(client):
    response = client.post(
        '/users/1/books',
        data={'title':'The Martian', 'author':'Andy Weir', 'isbn':'978-0-8041-3902-1', 'publication_date':'Feb 11 2014'}
    )
    assert response.status_code == 400

''' test FAILURE to add new book for known user with incomplete data
    parametrize iterates through for each book field being invalid '''
@pytest.mark.parametrize(('title', 'author', 'isbn', 'publication_date'), (
    ('', 'Emily St. John Mandel', '978-0-8041-7244-8', 'Jun 2, 2015'),
    ('Station Eleven', '', '978-0-8041-7244-8', 'Jun 2, 2015'),
    ('Station Eleven', 'Emily St. John Mandel', '', 'Jun 2, 2015'),
    ('Station Eleven', 'Emily St. John Mandel', '978-0-8041-7244-8', ''),
))
def test_add_book_bad_data(client, title, author, isbn, publication_date):
    response = client.post(
        '/users/1/books',
        data={'title':title, 'author':author, 'isbn':isbn, 'publication_date':publication_date}
    )
    assert response.status_code == 400

''' test SUCCESS to add new book for known user '''
def test_add_book(client):
    title = 'Station Eleven'
    author = 'Emily St. John Mandel'
    isbn = '978-0-8041-7244-8'
    publication_date = 'Jun 2, 2015'
    response = client.post(
        '/users/1/books',
        data={'title':title, 'author':author, 'isbn':isbn, 'publication_date':publication_date}
    )
    assert response.status_code == 201

    # test SUCCESS to retrieving the added book
    response = client.get('/users/1/books')
    assert response.status_code == 200
    assert title.encode('utf-8') in response.data
    assert isbn.encode('utf-8') in response.data
