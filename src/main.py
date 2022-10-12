from fastapi import FastAPI, Depends

from auth import get_user_token
from crud import add_document, get_document, change_document
from models import Account

app = FastAPI()


@app.get("/")
async def root(jwt: str = Depends(get_user_token)):
    return {"message": f"Hello {jwt['email']}"}


@app.post("/api/v1/account")
async def create_account(account: Account, jwt: str = Depends(get_user_token)):
    account.email = jwt['email']
    return add_document(jwt['uid'], account, 'accounts')


@app.get("/api/v1/account")
async def get_account(jwt: str = Depends(get_user_token)):
    return get_document(jwt['uid'], 'accounts')


@app.patch("/api/v1/account")
async def update_account(values: dict, jwt: str = Depends(get_user_token)):
    return change_document(jwt['uid'], 'accounts', values)
