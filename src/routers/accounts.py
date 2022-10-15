from fastapi import APIRouter, Depends

from auth import get_user_token
from firestore_db.collections import ACCOUNTS_COLLECTION
from firestore_db.crud import add_document, get_document, change_document
from models import Account

router = APIRouter(
    prefix="/api/v1/account",
    tags=["accounts"],
    dependencies=[Depends(get_user_token)],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def create_account(account: Account, jwt: str = Depends(get_user_token)):
    account.email = jwt['email']
    return add_document(jwt['uid'], account, ACCOUNTS_COLLECTION)


@router.get("")
async def get_account(jwt: str = Depends(get_user_token)):
    return get_document(jwt['uid'], ACCOUNTS_COLLECTION)


@router.patch("")
async def update_account(values: dict, jwt: str = Depends(get_user_token)):
    return change_document(jwt['uid'], ACCOUNTS_COLLECTION, values)
