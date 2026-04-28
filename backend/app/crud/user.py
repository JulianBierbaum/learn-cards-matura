from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password


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


def get_user_by_email(*, db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
 
    if not db_user:
        return None

    return db_user

