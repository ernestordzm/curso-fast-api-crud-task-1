
from fastapi.testclient import TestClient

from database.database import get_database_session
from api import app

client = TestClient(app)

app.dependency_overrides[get_database_session] = get_database_session

def test_sign_new_user() -> None:
    payload = {
        'email' : 'admintesttestclient4@admin.com',
        'name': 'Ernesto',
        'surname': 'Rodriguez',
        'website': 'https://www.elnorte.com/',
        'password': '12345'
    }

    response = client.post('/register', json=payload)

    assert response.status_code == 201
    assert response.json() == {
        'message': 'User created successfully'
    }

    # assert response.status_code == 201
    # data = response.json()
    # assert data['email'] == 'admintest@admin.com'
    # assert 'id' in data

def test_login_user() -> None:
    payload = {
        'username' : 'admintesttestclient4@admin.com',
        'password': '12345'
    }

    response = client.post('/token', data=payload)

    assert response.status_code == 200
    data = response.json()
    assert 'access_token' in data

def test_logout() -> None:
    headers = {
        'accept': 'application /json',
        'Content-Type': 'application /json',
        'Token': 'gdHkg_Zp1fOKG3F0KNwlTj41OnrRozw-nONXa1oVheg'
    }

    response = client.delete('/logout', headers = headers)

    assert response.status_code == 200
    assert response.json()['msj'] == 'Ok'