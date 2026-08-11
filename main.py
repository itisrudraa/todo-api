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


@app.patch("/mark/{todo_id}")
def mark(todo_id: int):
    if todo_id in todos:
        todo = todos[todo_id]
        todo["completed"] = True

        return {
            "todo": todo,
            "message" : "Maked"
        }
    else:
        return{
            "message": "invalid todo id"
        }
    
@app.patch("/edit/{todo_id}")
def edit_title(todo_id: int, title: str):
    if todo_id in todos:
        todo = todos[todo_id]
        todo["title"] = title

        return {
            "todo": todo,
            "message" : "title edited"
        }
    else:
        return{
            "message": "invalid todo id"
        }

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id in todos:
        return todos[todo_id]
    else:
        return{
            "message": "invalid todo id"
        }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id in todos:
        todo = todos.pop(todo_id, None)
        return{
            "todo": todo,
            "message": "todo deleted"
        }
    else:
        return{
            "message": "invalid todo id"
        }
