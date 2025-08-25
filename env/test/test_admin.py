from .utilis import *
from fastapi import status

def test_admin_read_all_authenticated(test_todo):
    response = client.get('/admin/todo')
    assert response.status_code == status.HTTP_200_OK
    # Just verify that the endpoint returns a list of todos
    todos = response.json()
    assert isinstance(todos, list)
    # If there are todos, verify they have the expected structure
    if todos:
        assert 'id' in todos[0]
        assert 'title' in todos[0]
        assert 'description' in todos[0]
        assert 'priority' in todos[0]
        assert 'complete' in todos[0]
        assert 'owner_id' in todos[0]