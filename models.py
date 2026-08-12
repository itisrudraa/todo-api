from pydantic import BaseModel

class Createtodo(BaseModel):
    title: str
    completed: bool = False

class Updatetodo(BaseModel):
    title: str | None = None
    completed: bool | None = None