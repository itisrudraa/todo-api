from fastapi import HTTPException, status, Request
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from db_models import Todo, User
from models import UserModel, LoginSchema
from utils.password import get_password_hash, verify_password
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError

load_dotenv()

engine = create_engine(os.getenv("DB_URL"))

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
    


def get_all_todos(user):
    return user.todos



def createTodo(title: str, completed: bool, user_id: int, db):
    todo = Todo(
        title = title,
        completed = completed,
        user_id = user_id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def updateTodo(todo_id: int, title: str | None, completed: bool | None, db, user_id):
    todo = db.get(Todo, todo_id)

    if todo is None:
        return None

    if todo.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    if title is not None:
        todo.title = title

    if completed is not None:
        todo.completed = completed

    db.commit()
    db.refresh(todo)
    return todo

def getTodo(todo_id: int, db, user_id: int):
    todo = db.get(Todo, todo_id)
    if todo is None:
        return None
    if todo.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return todo

def deleteTodo(todo_id: int, db, user_id:int):

    todo = db.get(Todo, todo_id)

    if todo is None:
        return None
    
    if todo.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized access")

    db.delete(todo)
    db.commit()
    return todo

def getUser(user_id: int, db):
    user = db.get(User, user_id)
    return user

def register_user(user: UserModel, db):

    is_user = db.execute(
        select(User).where(User.email == user.email)
    ).scalars().first()

    if is_user:
        raise HTTPException(status_code=400, detail="email already exist")

    new_user = User(
        username = user.username,
        email = user.email,
        password_hash = get_password_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body: LoginSchema, db):
    user = db.execute(
        select(User).where(User.email == body.email)
    ).scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")

    if not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong password")

    exp_time = datetime.now() + timedelta(int(os.getenv("EXP_TIME")))

    token = jwt.encode({"id": user.id, "exp":exp_time.timestamp()},os.getenv("SECRET_KEY"),os.getenv("ALGORITHM"))

    return {"token":token}
