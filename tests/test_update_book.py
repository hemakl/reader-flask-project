import pytest

''' test FAILURE to update book for unknown user '''
def test_update_book_user_not_found(client):
    response = client.put(
        '/users/99/books/1',
        data={'title':'The Martian', 'author':'Andy Weir', 'isbn':'978-0-8041-3902-1', 'publication_date':'Feb 11 2014'}
    )
    assert response.status_code == 404

''' test FAILURE to update book for incomplete data or different ISBN
    parametrize iterates through for each book field being invalid or a different ISBN '''
@pytest.mark.parametrize(('title', 'author', 'isbn', 'publication_date'), (
    ('', 'Andy Weir', '978-0-8041-3902-1', 'Feb 11 2014'),
    ('The Martian', '', '978-0-8041-3902-1', 'Feb 11 2014'),
    ('The Martian', 'Andy Weir', '', 'Feb 11 2014'),
    ('The Martian', 'Andy Weir', '978-0-8041-3902-1', ''),
    ('The Martian', 'Andy Weir', 'xxx-x-xxxx-xxxx-x', 'Feb 11 2014'),
))
def test_update_book_bad_data(client, title, author, isbn, publication_date):
    response = client.put(
        '/users/1/books/1',
        data={'title':title, 'author':author, 'isbn':isbn, 'publication_date':publication_date}
    )
    assert response.status_code == 400

''' test SUCCESS to update existing book
    parameterize iterates through for each field to update '''
@pytest.mark.parametrize(('title', 'author', 'isbn', 'publication_date'), (
    ('AMERICAN GODS', 'Neil Gaiman', '978-0062059888', 'Jun 21, 2011'),
    ('American Gods', 'Gaiman, Neil', '978-0062059888', 'Jun 21, 2011'),
    ('American Gods', 'Neil Gaiman', '978-0062059888', 'Apr 1, 2011'),
))
def test_update_book(client, title, author, isbn, publication_date):
    response = client.put(
        '/users/2/books/4',
        data={'title':title, 'author':author, 'isbn':isbn, 'publication_date':publication_date}
    )
    assert response.status_code == 200

    # check that each field is correct post update
    response = client.get('/users/2/books/4')
    assert response.status_code == 200
    assert title.encode('utf-8') in response.data
    assert author.encode('utf-8') in response.data
    assert isbn.encode('utf-8') in response.data
    assert publication_date.encode('utf-8') in response.data

