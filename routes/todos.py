from fastapi import APIRouter, HTTPException, Depends
from models import Createtodo, Updatetodo, todoResponse, Todo
from database import get_all_todos, createTodo, updateTodo, getTodo, deleteTodo, get_db, getUser
from utils.helper import is_authenticated

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("", response_model=list[Todo])
def get_todos(user=Depends(is_authenticated)):
    return get_all_todos(user)

@router.post("", response_model=todoResponse)
def create_todo(newtodo: Createtodo, db=Depends(get_db), user=Depends(is_authenticated)):
    todo = createTodo(newtodo.title, newtodo.completed, user.id, db)

    return{
        "todo": todo,
        "message": "todo added"
    }


@router.patch("/{todo_id}", response_model=todoResponse)
def update_todo(todo_id: int, update: Updatetodo, db=Depends(get_db), user = Depends(is_authenticated)):

    todo = updateTodo(todo_id, update.title, update.completed, db, user.id)
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
def get_todo(todo_id: int, db=Depends(get_db), user=Depends(is_authenticated)):
    todo = getTodo(todo_id, db, user.id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return todo

@router.delete("/{todo_id}", response_model=todoResponse)
def delete_todo(todo_id: int, user=Depends(is_authenticated), db=Depends(get_db)):
    todo = deleteTodo(todo_id, db, user.id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo ID"
        )

    return{
        "todo": todo,
        "message": "todo deleted"
    }
