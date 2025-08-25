from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
import sys
import os
import pytest
from .utilis import *

# Add the parent directory to the path so we can import from env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from routers.todos import get_db, get_current_user
from fastapi.testclient import TestClient
from fastapi import status
from models import Todos
from database import Base, engine, SessionLocal


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user



def test_read_all_authenticated(test_todo):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        # The test_create_todo is likely failing because the test_todo fixture creates a todo before the test runs,
        # so when test_create_todo posts a new todo, the database already contains one todo.
        # The test_read_all_authenticated expects only one todo with id=1, but after test_create_todo runs,
        # there may be more than one todo in the database, or the ids may not match.
        # To fix this, ensure the database is clean before each test, or adjust the test to account for multiple todos.
        'complete': False, 
        'title': "Need to learn everyday!", 
        'description': "Need to learn everyday!",
        'priority': 5, 
        'owner_id': 1, 
        'id': 1
    }]

def test_create_todo(test_todo):
    request_data={
        'title': "new Todo",
        'description': "new todo desc",
        'priority': 5,
        'complete': False

    }
    response = client.post('/todo', json=request_data)
    assert  response.status_code == 201






