import psycopg
import os
from psycopg.rows import dict_row
from dotenv import load_dotenv
from models import Updatetodo

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def get_all_todos():
    conn = get_connection()
    cur = conn.cursor(row_factory=dict_row)
    cur.execute("SELECT * FROM todos ORDER BY id ASC;")
    todos = cur.fetchall()
    cur.close()
    conn.close()
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