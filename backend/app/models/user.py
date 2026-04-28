from typing import List
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped
from app.database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    cards: Mapped[List["Card"]] = relationship(back_populates="user")
