from fastapi import APIRouter, HTTPException
from models import Createtodo, Updatetodo, todoResponse, Todo
import data


router = APIRouter(tags=["Todos"])

@router.get("/todos")
def get_todos():
    return data.todos

@router.post("/todos", response_model=todoResponse)
def create_todo(newtodo: Createtodo):
    new_id = data.next_id
    data.next_id += 1
    data.todos[new_id] = newtodo.model_dump()

    return {
        "todo": data.todos[new_id],
        "message" : "todo created"
    }


@router.patch("/todos/{todo_id}", response_model=todoResponse)
def update_todo(todo_id: int, update: Updatetodo):
    if todo_id not in data.todos:
        raise HTTPException(
            status_code= 404,
            detail="Invalid Todo ID"
        )

    todo = data.todos[todo_id]

    if update.title is not None:
        todo["title"] = update.title

    if update.completed is not None:
        todo["completed"] = update.completed

    return{
        "todo": todo,
        "message": "todo updated"
    }

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id in data.todos:
        return data.todos[todo_id]
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )

@router.delete("/todos/{todo_id}", response_model=todoResponse)
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

