from fastapi import APIRouter, HTTPException, Depends
from models import Createtodo, Updatetodo, todoResponse, Todo
import data


router = APIRouter(prefix="/todos", tags=["Todos"])

def get_todo_dependency(todo_id: int):
    if todo_id not in data.todos:
        raise HTTPException(
            status_code=404,
            detail="Inavlid Todo ID"
        )
    todo = data.todos[todo_id]
    return todo

@router.get("")
def get_todos():
    return data.todos

@router.post("", response_model=todoResponse)
def create_todo(newtodo: Createtodo):
    new_id = data.next_id
    data.next_id += 1
    data.todos[new_id] = newtodo.model_dump()

    return {
        "todo": data.todos[new_id],
        "message" : "todo created"
    }


@router.patch("/{todo_id}", response_model=todoResponse)
def update_todo(update: Updatetodo, todo = Depends(get_todo_dependency)):

    if update.title is not None:
        todo["title"] = update.title

    if update.completed is not None:
        todo["completed"] = update.completed

    return{
        "todo": todo,
        "message": "todo updated"
    }

@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo = Depends(get_todo_dependency)):
    return todo

@router.delete("/{todo_id}", response_model=todoResponse)
def delete_todo(todo_id: int, todo = Depends(get_todo_dependency)):
    data.todos.pop(todo_id)
    return{
        "todo": todo,
        "message": "todo deleted"
    }
