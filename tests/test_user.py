import pytest

''' test FAILURE to retrieve unknown user '''
def test_get_user_not_found(client):
    response = client.get('/users/19')
    assert response.status_code == 404

''' test SUCCESS to retrieve known user '''
def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert b'Eloi' in response.data
    assert b'Wells' in response.data
    assert b'1a2b3c4d' not in response.data
    assert b'eloi@mutiny.com' in response.data

''' test FAILURE to update user with bad data '''
@pytest.mark.parametrize(('firstname', 'lastname', 'email', 'password'), (
    ('', 'Wells', 'eloi@mutiny.com', 'password1'),
    ('Eloi', '', 'eloi@mutiny.com', 'password1'),
    ('Eloi', 'Wells', '', 'password1'),
    ('Eloi', 'Wells', 'eloi@mutiny.com', ''),
))
def test_update_user_bad_data(client, firstname, lastname, email, password):
    response = client.put(
        '/users/1',
        data = {'firstname':firstname, 'lastname':lastname, 'email':email, 'password':password}
    )
    assert response.status_code == 400

''' test FAILURE to update unknown user '''
def test_update_user_not_found(client):
    response = client.put(
        '/users/25',
        data = {'firstname':'Eloi', 'lastname':'Wells', 'email':'eloi@mutiny.com', 'password':'password1'}
    )
    assert response.status_code == 404

''' test SUCCESS to update known user '''
def test_update_user(client):
    response = client.put(
        '/users/1',
        data = {'firstname':'Elle', 'lastname':'Wells', 'email':'eloi@mutiny.com', 'password':'password1'}
    )
    assert response.status_code == 200

    # check the user has updated info
    response = client.get('/users/1')
    assert b'Elle' in response.data
    assert b'Eloi' not in response.data

''' test FAILURE to authenticate to update user '''
def test_update_user_unauthenticated(client):
    response = client.put(
        '/users/1',
        data = {'firstname':'Elle', 'lastname':'Wells', 'email':'eloi@mutiny.com', 'password':'passwordX'}
    )
    assert response.status_code == 401

    #check the user does not have update info
    response = client.get('/users/1')
    assert b'Elle' not in response.data
    assert b'Eloi' in response.data

''' test FAILURE to delete unknown user '''
def test_delete_user_not_found(client):
    response = client.delete('/users/13')
    assert response.status_code == 404

''' test SUCCESS to delete known user '''
def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204

    #check the user is deleted
    response = client.get('/users/1')
    assert response.status_code == 404

''' test FAILURE to add user with bad data '''
@pytest.mark.parametrize(('firstname', 'lastname', 'email', 'password'), (
    ('', 'Chuzzleworth', 'martin@charlesdickens.com', 'badpasswd'),
    ('Martin', '', 'martin@charlesdickens.com', 'badpasswd'),
    ('Martin', 'Chuzzleworth', '', 'badpasswd'),
    ('Martin', 'Chuzzleworth', 'martin@charlesdickens.com', ''),
))
def test_add_user_bad_data(client, firstname, lastname, email, password):
    response = client.post(
        '/users',
        data = {'firstname':firstname, 'lastname':lastname, 'email':email, 'password':password}
    )
    assert response.status_code == 400

''' test SUCCESS to add user '''
def test_add_user(client):
    response = client.post(
        '/users',
        data = {'firstname':'Martin', 'lastname':'Chuzzleworth', 'email':'martin@charlesdickens.com', 'password':'badpasswd'}
    )
    assert response.status_code == 201

    #check user exists
    response = client.get('/users/3')
    assert response.status_code == 200
    assert b'Martin' in response.data

''' test FAILURE to add existing user '''
def test_update_user_exists(client):
    response = client.post(
        '/users',
        data = {'firstname':'Martin', 'lastname':'Chuzzleworth', 'email':'eloi@mutiny.com', 'password':'badpasswd'}
    )
    assert response.status_code == 400

''' test FAILURE to find any users '''
def test_get_users_none(client):
    client.delete('/users/1')
    client.delete('/users/2')
    response = client.get('/users')
    assert response.status_code == 404
