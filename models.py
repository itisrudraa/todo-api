from pydantic import BaseModel, ConfigDict, EmailStr

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

# user models

class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponseModel(BaseModel):
    id: int
    username: str
    email: EmailStr

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
