from pydantic import BaseModel

class Createtodo(BaseModel):
    title: str
    status: bool = False