from pydantic import BaseModel, ConfigDict

class Createtodo(BaseModel):
    title: str
    completed: bool = False

class Updatetodo(BaseModel):
    title: str | None = None
    completed: bool | None = None

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)

class todoResponse(BaseModel):
    todo: Todo
    message: str