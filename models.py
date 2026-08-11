from pydantic import BaseModel

class Createtodo(BaseModel):
    title: str
    completed: bool = False