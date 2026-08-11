from fastapi import FastAPI, HTTPException
import data
from models import Createtodo, Updatetodo
app = FastAPI()

@app.get("/")
def home():
    return {"message": "server has started"}
  
@app.get("/todos")
def get_todos():
    return data.todos

@app.post("/todos")
def create_todo(newtodo: Createtodo):
    new_id = data.next_id
    data.next_id += 1
    data.todos[new_id] = newtodo.model_dump()

    return {
        "todo": data.todos[new_id],
        "message" : "todo created"
    }


@app.patch("/mark/{todo_id}")
def mark(todo_id: int):
    if todo_id in data.todos:
        todo = data.todos[todo_id]
        todo["completed"] = True

        return {
            "todo": todo,
            "message" : "Maked"
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )
    
@app.patch("/edit/{todo_id}")
def edit_title(todo_id: int, ntodo: Updatetodo):
    if todo_id in data.todos:
        todo = data.todos[todo_id]
        tdo = ntodo.model_dump()
        todo["title"] = tdo["title"]

        return {
            "todo": todo,
            "message" : "title edited"
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id in data.todos:
        return data.todos[todo_id]
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id in data.todos:
        todo = data.todos.pop(todo_id, None)
        return{
            "todo": todo,
            "message": "todo deleted"
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )
