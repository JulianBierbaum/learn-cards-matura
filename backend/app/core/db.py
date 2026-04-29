from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import settings

from app.database.session import Base, engine
from app.schemas.user import UserCreate
from app.crud.user import create_admin, create_user

# models must be imported and registered from app.models to create the tables
from app.models.user import User


def init_db(session: Session) -> None:
    """
    Initialize the database by creating tables and a superuser if it doesn't exist.

    Args:
      session (Session): The database session used to interact with the database.
    """
    # Create tables
    Base.metadata.create_all(bind=engine)

    seed_users(session=session)


def seed_users(session: Session) -> None:
    """
    Seed the database with initial user data.

    Args:
      session (Session): The database session used to interact with the database.
    """
    # Create admin
    admin = session.execute(
        select(User).where(User.email == settings.FIRST_SUPERUSER_EMAIL)
    ).first()

    if not admin:
        user_in = UserCreate(
            name=settings.FIRST_SUPERUSER,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
        )
        _ = create_admin(db=session, user=user_in)

    # Create regular user
    user = session.execute(
        select(User).where(User.email == settings.FIRST_USER_EMAIL)
    ).first()

    if not user:
        user_in = UserCreate(
            name=settings.FIRST_USER,
            email=settings.FIRST_USER_EMAIL,
            password=settings.FIRST_USER_PASSWORD,
        )
        _ = create_user(db=session, user=user_in)
