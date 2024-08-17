from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=120)
    email: EmailStr
