import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient
from passlib.context import CryptContext

from app.database.session import Base
from app.main import app
from app.api.deps import get_db, get_current_user
from app.models.user import User
import shutil
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
ALGORITHM = "HS256"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@pytest.fixture(scope="function")
def db():
    """Creates a new database session and ensures tables exist."""
    Base.metadata.create_all(bind=engine)  
    session = TestingSessionLocal()
    try:
        yield session  
    finally:
        if os.path.exists(SQLALCHEMY_DATABASE_URL.replace("sqlite:///", "")):
            shutil.copy(SQLALCHEMY_DATABASE_URL.replace("sqlite:///", ""), f"backup.{SQLALCHEMY_DATABASE_URL.replace('sqlite:///', '')}")
        session.rollback()
        session.close()
        Base.metadata.drop_all(bind=engine)  

@pytest.fixture(scope="function")
def client(db):
    """Provides a FastAPI test client using the same session as the test."""
    
    def override_get_db():
        Base.metadata.create_all(bind=engine) 
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
    

@pytest.fixture
def client_with_superuser(client, test_admin):
    """Override `get_current_user` to return an admin user."""
    def override_get_current_user():
        return test_admin  
    
    app.dependency_overrides[get_current_user] = override_get_current_user
    return client

@pytest.fixture
def client_without_superuser(client, test_client):
    """Override `get_current_user` to return a non-admin user."""
    def override_get_current_user():
        return test_client  
    
    app.dependency_overrides[get_current_user] = override_get_current_user
    return client

@pytest.fixture
def test_admin(db):
    """Creates an admin user in the test database."""
    user = User(name="admin", email="admin@test.com", hashed_password=hash_password("Kennwort1"), is_admin=True)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def test_client(db):
    """Creates an user in the test database."""
    user = User(name="client", email="client@test.com", hashed_password=hash_password("Kennwort1"), is_admin=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

