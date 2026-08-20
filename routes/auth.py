from fastapi import APIRouter, HTTPException, Depends
from models import UserModel, UserResponseModel, LoginSchema
from database import register_user, get_db, login_user

auth_router = APIRouter(prefix="/user")

@auth_router.post("/register", response_model=UserResponseModel)
def register(user: UserModel, db = Depends(get_db)):
    return register_user(user, db)

@auth_router.post("/login")
def login(body: LoginSchema, db = Depends(get_db)):
    return login_user(body, db)