from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
