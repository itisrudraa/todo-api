from fastapi import APIRouter, HTTPException, Depends
from models import Createtodo, Updatetodo, todoResponse, Todo
from database import get_all_todos, createTodo, updateTodo, getTodo, deleteTodo, get_db


router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("", response_model=list[Todo])
def get_todos(db=Depends(get_db)):
    return get_all_todos(db)

@router.post("", response_model=todoResponse)
def create_todo(newtodo: Createtodo, db=Depends(get_db)):
    todo = createTodo(newtodo.title, newtodo.completed, db)

    return{
        "todo": todo,
        "message": "todo added"
    }


@router.patch("/{todo_id}", response_model=todoResponse)
def update_todo(todo_id: int, update: Updatetodo, db=Depends(get_db)):

    todo = updateTodo(todo_id, update.title, update.completed, db)
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
def get_todo(todo_id: int, db=Depends(get_db)):
    todo = getTodo(todo_id, db)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return todo

@router.delete("/{todo_id}", response_model=todoResponse)
def delete_todo(todo_id: int, db=Depends(get_db)):
    todo = deleteTodo(todo_id, db)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return{
        "todo": todo,
        "message": "todo deleted"
    }
