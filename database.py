from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models import Updatetodo
from db_models import Todo

load_dotenv()

engine = create_engine(os.getenv("DB_URL"))

SessionLocal = sessionmaker(bind=engine)




def get_all_todos():
    db = SessionLocal()
    result = db.execute(
        select(Todo)
    )
    todos = result.scalars().all()
    db.close()
    return todos



def createTodo(title: str, completed: bool):
    conn = get_connection()
    cur = conn.cursor(row_factory=dict_row)
    cur.execute("INSERT INTO todos (title, completed) VALUES (%s, %s) RETURNING id, title, completed",(title, completed))
    todo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return todo

def updateTodo(todo_id: int, title: str | None, completed: bool | None):
   conn = get_connection()
   cur = conn.cursor(row_factory=dict_row)
   cur.execute("UPDATE todos SET title=COALESCE(%s, title), completed=COALESCE(%s, completed) WHERE id=%s RETURNING id, title, completed", (title, completed, todo_id))
   todo = cur.fetchone()
   conn.commit()
   cur.close()
   conn.close()
   return todo

def getTodo(todo_id: int):
    conn = get_connection()
    cur = conn.cursor(row_factory=dict_row)
    cur.execute("SELECT id, title, completed FROM todos WHERE id=%s", (todo_id,))
    todo = cur.fetchone()
    cur.close()
    conn.close()
    return todo

def deleteTodo(todo_id: int):
    conn = get_connection()
    cur = conn.cursor(row_factory=dict_row)
    cur.execute("DELETE FROM todos WHERE id=%s RETURNING id, title, completed", (todo_id,))
    todo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return todo