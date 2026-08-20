from fastapi import FastAPI
from routes.todos import router
from routes.auth import auth_router
app = FastAPI()

@app.get("/")
def home():
    return {"message": "server has started"}
  
app.include_router(router)
app.include_router(auth_router)
