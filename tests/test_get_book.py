import pytest

''' test FAILURE to retrieve books for unknown user '''
def test_get_wishlist_user_not_found(client):
    assert client.get('/users/7/books').status_code == 404

''' test SUCCESS to retrieve books for known user
    parametrize iterates through each known user '''
@pytest.mark.parametrize(('path', 'title1', 'title2', 'title3'), (
    ('/users/1/books', b'The Martian', b'The Cathedral and the Bazaar', b''),
    ('/users/2/books', b'Ready Player One', b'American Gods', b'The Painted Veil'),
))
def test_get_wishlist(client, path, title1, title2, title3):
    response = client.get(path)
    assert response.status_code == 200

    # check that each title is returned
    assert title1 in response.data
    assert title2 in response.data
    assert title3 in response.data

''' test FAILURE to retrieve a book for unknown user '''
def test_get_book_user_not_found(client):
    assert client.get('/users/99/books/1').status_code == 404

''' test FAILURE to retrieve a book not on user wishlist '''
def test_get_book_book_not_found_for_user(client):
    assert client.get('/users/1/books/3').status_code == 404

''' test SUCCESS to retrieve a book for user
    parametrize iterates through each existing book for each known user '''
@pytest.mark.parametrize(('path', 'title', 'author', 'isbn', 'date'), (
    ('/users/1/books/1', b'The Martian', b'Andy Weir', b'978-0-8041-3902-1', b'Feb 11 2014'),
    ('/users/1/books/2', b'The Cathedral and the Bazaar', b'Eric S. Raymond', b'978-0-596-00108-7', b'Feb 1 2001'),
    ('/users/2/books/3', b'Ready Player One', b'Ernest Cline', b'978-0307887443', b'Jun 5, 2012'),
    ('/users/2/books/4', b'American Gods', b'Neil Gaiman', b'978-0062059888', b'Jun 21, 2011'),
    ('/users/2/books/5', b'The Painted Veil', b'W. Somerset Maugham', b'978-0307277770', b'Nov 14, 2006'),
))
def test_get_book(client, path, title, author, isbn, date):
    response = client.get(path)
    assert response.status_code == 200

    # check that each field is matching
    assert title in response.data
    assert author in response.data
    assert isbn in response.data
    assert date in response.data
