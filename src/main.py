from fastapi import FastAPI
from crud import add_document, find_document, change_document
from models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/api/v1/user")
async def create_user(user: User):
    return add_document(user, 'users')

@app.get("/api/v1/user/{id}")
async def get_user(id: str):
    return find_document(id, 'users')

@app.patch("/api/v1/user/{id}")
async def update_user(id: str, values: dict):
    return change_document(id, 'users', values)