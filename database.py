from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from db_models import Todo

load_dotenv()

engine = create_engine(os.getenv("DB_URL"))

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
    


def get_all_todos(db):
    result = db.execute(
        select(Todo).order_by(Todo.id)
    )
    todos = result.scalars().all()
    return todos



def createTodo(title: str, completed: bool, db):
    todo = Todo(
        title = title,
        completed = completed
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def updateTodo(todo_id: int, title: str | None, completed: bool | None, db):
    todo = db.get(Todo, todo_id)

    if todo is None:
        return None

    if title is not None:
        todo.title = title

    if completed is not None:
        todo.completed = completed

    db.commit()
    db.refresh(todo)
    return todo

def getTodo(todo_id: int, db):
    todo = db.get(Todo, todo_id)
    return todo

def deleteTodo(todo_id: int, db):

    todo = db.get(Todo, todo_id)
    if todo is None:
        return None
    db.delete(todo)
    db.commit()
    return todo