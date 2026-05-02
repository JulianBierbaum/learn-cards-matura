from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from app.models.enum import LearnState


class CardBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=25)
    front: str = Field(..., min_length=1, max_length=500)
    back: str = Field(..., min_length=1, max_length=500)
    tags: Optional[List[str]] = Field(None)
    learnState: LearnState = Field(...)


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=25)
    front: Optional[str] = Field(None, min_length=1, max_length=500)
    back: Optional[str] = Field(None, min_length=1, max_length=500)
    tags: Optional[List[str]] = Field(None)
    learnState: Optional[LearnState] = Field(None)


class Card(CardBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
