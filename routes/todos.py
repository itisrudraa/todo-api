from fastapi import APIRouter, HTTPException
from models import Createtodo, Updatetodo, todoResponse, Todo
from database import get_all_todos, createTodo, updateTodo, getTodo, deleteTodo


router = APIRouter(prefix="/todos", tags=["Todos"])

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
def update_todo(todo_id: int, update: Updatetodo):

    todo = updateTodo(todo_id, update.title, update.completed)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return{
        "todo": todo,
        "message": "todo updated"
    }

@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = getTodo(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return todo

@router.delete("/{todo_id}", response_model=todoResponse)
def delete_todo(todo_id: int):
    todo = deleteTodo(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return{
        "todo": todo,
        "message": "todo deleted"
    }
