from fastapi import FastAPI
from data import todos

app = FastAPI()

@app.get("/")
def home():
    return {"message": "server has started"}



