from fastapi import APIRouter, HTTPException, Depends
from models import Createtodo, Updatetodo, todoResponse, Todo
import data
from database import get_all_todos, createTodo


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
    return get_all_todos()

@router.post("", response_model=todoResponse)
def create_todo(newtodo: Createtodo):
    todo = createTodo(newtodo.title, newtodo.completed)

    return{
        "todo": todo,
        "message": "todo added"
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
