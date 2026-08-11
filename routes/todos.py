from fastapi import APIRouter, HTTPException
from models import Createtodo, Updatetodo
import data


router = APIRouter(tags=["Todos"])

@router.get("/todos")
def get_todos():
    return data.todos

@router.post("/todos")
def create_todo(newtodo: Createtodo):
    new_id = data.next_id
    data.next_id += 1
    data.todos[new_id] = newtodo.model_dump()

    return {
        "todo": data.todos[new_id],
        "message" : "todo created"
    }


@router.patch("/mark/{todo_id}")
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
    
@router.patch("/edit/{todo_id}")
def edit_title(todo_id: int, ntodo: Updatetodo):
    if todo_id in data.todos:
        todo = data.todos[todo_id]
        todo["title"] = ntodo.title

        return {
            "todo": todo,
            "message" : "title edited"
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id in data.todos:
        return data.todos[todo_id]
    else:
        raise HTTPException(
            status_code=404,
            detail="Invalid todo id"
        )

@router.delete("/todos/{todo_id}")
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

