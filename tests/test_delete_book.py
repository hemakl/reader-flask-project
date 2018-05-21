import pytest

''' test FAILURE to delete book from unknown user '''
def test_delete_book_user_not_found(client):
    response = client.delete('/users/99/books/1')
    assert response.status_code == 404

''' test FAILURE to delete book not on known user wishlist '''
def test_delete_book_not_found_for_user(client):
    response = client.delete('/users/2/books/2')
    assert response.status_code == 404

''' test SUCCESS to delete book '''
def test_delete_book(client):
    response = client.delete('/users/1/books/2')
    assert response.status_code == 204

    # check FAILURE to retrieve deleted book
    response = client.get('/users/1/books/2')
    assert response.status_code == 404

    # check FAILURE to find book in user test_get_wishlist
    response = client.get('/users/1/books')
    assert response.status_code == 200
    assert b'The Cathedral and the Bazaar' not in response.data

''' test FAILURE to delete all books from unknown user '''
def test_delete_wishlist_user_not_found(client):
    response = client.delete('/users/33/books')
    assert response.status_code == 404

''' test SUCCESS to delete book '''
def test_delete_wishlist(client):
    response = client.delete('/users/1/books')
    assert response.status_code == 204

    # check FAILURE to retrieve books for user
    response = client.get('/users/1/books')
    assert response.status_code == 404
