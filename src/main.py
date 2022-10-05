from fastapi import FastAPI
from crud import add_user
from models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/api/v1/user")
async def create_user(user: User):
    return add_user(user)