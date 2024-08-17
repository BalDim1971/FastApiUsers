from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt

router = APIRouter()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post('/token', response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Например, проверяем имя пользователя и пароль в базе данных (упрощено)
    if form_data.username != "testuser" or form_data.password != "testpassword":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Если все хорошо, создаем токен
    access_token = create_jwt_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
