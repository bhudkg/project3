from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
import sys
import os
import pytest

# Add the parent directory to the path so we can import from env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from fastapi.testclient import TestClient
from models import Todos
from database import Base, engine, SessionLocal
from routers.auth import get_current_user
from routers.todos import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'testuser', 'id': 1, 'user_role': 'admin'}


# Set up dependency overrides
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

@pytest.fixture
def test_todo():
    # Clean up the test database first
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    todo = Todos(
        title="Need to learn everyday!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    db.refresh(todo)
    yield todo
    db.close()