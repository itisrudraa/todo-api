from fastapi import FastAPI
from routes.todos import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "server has started"}
  
app.include_router(router)
