from fastapi import FastAPI
from data import todos
from models import Createtodo
app = FastAPI()

@app.get("/")
def home():
    return {"message": "server has started"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/create")
def create_todo(newtodo: Createtodo):
    new_id = len(todos)+1
    todos[new_id] = newtodo.model_dump()

    return {
        "todo": todos[new_id],
        "message" : "todo created"
    }
    

