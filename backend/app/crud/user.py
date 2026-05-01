from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from app.exceptions.user import (
    UserDatabaseException,
    MissingUserException,
    DuplicateUserException,
)


def authenticate_user(*, db: Session, email: str, password: str):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        return None
    if not verify_password(password, str(db_user.hashed_password)):
        return None
    return db_user


def create_user(*, db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        is_admin=False,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_admin(*, db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        is_admin=True,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(*, db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_users(*, db: Session) -> List[User]:
    return db.query(User).all()


def get_user_by_email(*, db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update_user(*, db: Session, user_id: int, user: UserUpdate) -> User:
    db_user = get_user(db=db, user_id=user_id)

    if not db_user:
        raise MissingUserException(user_id=user_id)

    try:
        if user.name is not None:
            db_user.name = user.name

        if user.email is not None:
            db_user.email = user.email

        if user.is_admin is not None:
            db_user.is_admin = user.is_admin

        if user.password is not None:
            db_user.hashed_password = get_password_hash(user.password)

        db.commit()
        db.refresh(db_user)
        return db_user

    except IntegrityError as e:
        db.rollback()

        if "unique" in str(e).lower():
            raise DuplicateUserException(name=user.name, email=user.email)
        else:
            raise UserDatabaseException(err=str(e))
