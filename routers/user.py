from fastapi import APIRouter, HTTPException
from schemas.user import User, UserCreate
from services.user_service import (fetch_users, fetch_user_by_id,
                                   add_user, delete_user)
from typing import List

router = APIRouter()


@router.get("/users/", response_model=List[User])
async def get_users():
    return await fetch_users()


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await fetch_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    new_user = await add_user(user)
    if new_user is None:
        raise HTTPException(status_code=400, detail='User already exists')
    return new_user


@router.delete("/users/{user_id}")
async def delete_user_route(user_id: int):
    result = await delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail='User not found')
    return {'message': 'User deleted'}
