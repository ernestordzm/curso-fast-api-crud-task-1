
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from database.task import crud
from database import models
from api import app
from database.database import get_database_session

client = TestClient(app)
app.dependency_overrides[get_database_session] = get_database_session

def test_create_task() -> None:
    payload = {
        'name': 'Task 1 FaspAPI',
        'description': 'Description Task',
        'status': 'done',
        'user_id': '1',
        'category_id': '1'
    }

    response = client.post('/task/', json=payload)
    assert response.status_code == 201
    assert response.json()['tasks']['name'] == payload['name']

def test_create_task_form_data() -> None:
    payload = {
        'name': 'Task 1 FaspAPI FD',
        'description': 'Description Task FD',
        'status': 'done',
        'user_id': '1',
        'category_id': '1'
    }

    response = client.post('/task/form-create', data=payload)
    assert response.status_code == 201
    assert response.json()['tasks']['name'] == payload['name']

def test_update_task() -> None:
    payload = {
        'id': '2',
        'name': 'Task 1 FaspAPI Upd',
        'description': 'Description Task',
        'status': 'done',
        'user_id': '1',
        'category_id': '1'
    }

    response = client.put('/task/'+payload['id'], json=payload)
    assert response.status_code == 200
    assert response.json()['tasks']['name'] == payload['name']


def test_all_tasks(db: Session = next(get_database_session())) -> None:
    tasks = crud.getAll(db)
    response = client.get('/task/')

    assert response.status_code == 200
    assert len(tasks) == len(response.json()['task'])

def test_by_id(db: Session = next(get_database_session())) -> None:
    id = 2
    task = crud.getById(id, db)

    response = client.get('/task/'+str(id))

    assert response.status_code == 200
    assert id == response.json()['id']
    assert task.name == response.json()['name']

def test_delete_task(db: Session = next(get_database_session())) -> None:
    id = 3
    response = client.delete('/task/'+str(id))

    task = db.query(models.Task).get(id)
    assert response.status_code == 200
    assert task is None
    assert 'Ok' == response.json()['msj']

def test_delete_task_not_exist(db: Session = next(get_database_session())) -> None:
    id = 3
    response = client.delete('/task/'+str(id))

    task = db.query(models.Task).get(id)
    assert response.status_code == 404
    assert task is None
    # assert 'Ok' == response.json()['msj']

