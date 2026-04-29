from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=15)
    email: EmailStr = Field(..., min_length=7, max_length=50)
    is_admin: Optional[bool] = False
    password: str = Field(..., min_length=1, max_length=50)


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=15)
    email: Optional[EmailStr] = Field(None, min_length=7, max_length=50)
    is_admin: Optional[bool] = False
    password: Optional[str] = Field(None, min_length=1, max_length=50)


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=15)
    email: EmailStr = Field(..., min_length=7, max_length=50)
    is_admin: Optional[bool] = False
    model_config = ConfigDict(from_attributes=True)
