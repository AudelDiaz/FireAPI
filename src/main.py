from fastapi import FastAPI, Header

from auth import get_uid
from crud import add_document, find_document, change_document
from models import User

app = FastAPI()


@app.get("/")
async def root(authorization: str = Header(None)):
    if get_uid(authorization):
        return {"message": f"Hello {get_uid(authorization)}"}


@app.post("/api/v1/user")
async def create_user(user: User, authorization: str = Header(None)):
    if get_uid(authorization):
        return add_document(user, 'users')


@app.get("/api/v1/user/{id}")
async def get_user(id: str, authorization: str = Header(None)):
    if get_uid(authorization):
        return find_document(id, 'users')


@app.patch("/api/v1/user/{id}")
async def update_user(id: str, values: dict, authorization: str = Header(None)):
    if get_uid(authorization):
        return change_document(id, 'users', values)
