from sqlalchemy.exc import IntegrityError

from app.models.base import Base
from app.models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

@pytest.fixture(scope="function")
def db_session():
    """Fixture to provide a test database session."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db_session):
    """Test creation and validation of User model."""
    user = User(username="testuser", email="test@example.com", hashed_password="hashedpass")
    db_session.add(user)
    db_session.commit()
    fetched = db_session.query(User).first()
    assert fetched.username == "testuser"
    assert fetched.email == "test@example.com"
    assert fetched.is_active is True

def test_unique_username(db_session):
    """Test creation and validation of User model."""
    user1 = User(username="testuser", email="test1@example.com", hashed_password="hashedpass")
    db_session.add(user1)
    db_session.commit()
    user2 = User(username="testuser", email="test2@example.com", hashed_password="hashedpass")
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

def test_unique_email(db_session):
    user1 = User(username="testuser1", email="test@example.com", hashed_password="hashedpass")
    db_session.add(user1)
    db_session.commit()
    user2 = User(username="testuser", email="test@example.com", hashed_password="hashedpass")
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()