from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey, JSON, Enum as pgEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.session import Base
from app.models.enum import LearnState


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    front: Mapped[str] = mapped_column(String, nullable=False)
    back: Mapped[str] = mapped_column(String, nullable=False)
    tags: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=True)
    learnState: Mapped[LearnState] = mapped_column(pgEnum(LearnState), nullable=False)

    user = relationship("User", back_populates="cards")
