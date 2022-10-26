from string import Template

from fastapi import APIRouter, Depends

from auth import get_user_token
from firestore_db.collections import ADDRESSES_COLLECTION
from firestore_db.crud import add_document, get_document, get_collection_documents, remove_document, change_document
from models import Address

router = APIRouter(
    prefix="/api/v1/account/addresses",
    tags=["addresses"],
    dependencies=[Depends(get_user_token)],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def create_address(address: Address, jwt: dict = Depends(get_user_token)):
    return add_document(None, address, Template(ADDRESSES_COLLECTION).safe_substitute(uid=jwt['uid']))


@router.get("/{id}")
async def get_address(id: str, jwt: dict = Depends(get_user_token)):
    return get_document(id, Template(ADDRESSES_COLLECTION).safe_substitute(uid=jwt['uid']))


@router.get("")
async def get_addresses(jwt: dict = Depends(get_user_token)):
    return get_collection_documents(Template(ADDRESSES_COLLECTION).safe_substitute(uid=jwt['uid']))


@router.delete("/{id}")
async def delete_address(id: str, jwt: dict = Depends(get_user_token)):
    return remove_document(id, Template(ADDRESSES_COLLECTION).safe_substitute(uid=jwt['uid']))


@router.patch("/{id}")
async def update_address(id: str, values: dict, jwt: dict = Depends(get_user_token)):
    return change_document(id, Template(ADDRESSES_COLLECTION).safe_substitute(uid=jwt['uid']), values)
