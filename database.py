import psycopg
import os
from psycopg.rows import dict_row
from dotenv import load_dotenv

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
    cur.execute("SELECT * FROM todos")
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
    