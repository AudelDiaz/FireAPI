from fastapi import APIRouter, Depends

from auth import get_user_token
from firestore_db.collections import ADDRESSES_COLLECTION
from firestore_db.crud import add_document, get_document, get_collection_documents, remove_document
from models import Address

router = APIRouter(
    prefix="/api/v1/account/address",
    tags=["addresses"],
    dependencies=[Depends(get_user_token)],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def create_address(address: Address, jwt: str = Depends(get_user_token)):
    return add_document(None, address, ADDRESSES_COLLECTION.format(uid=jwt['uid']))


@router.get("/{id}")
async def get_address(id: str, jwt: str = Depends(get_user_token)):
    return get_document(id, ADDRESSES_COLLECTION.format(uid=jwt['uid']))


@router.get("")
async def get_addresses(jwt: str = Depends(get_user_token)):
    return get_collection_documents(ADDRESSES_COLLECTION.format(uid=jwt['uid']))


@router.delete("/{id}")
async def get_address(id: str, jwt: str = Depends(get_user_token)):
    return remove_document(id, ADDRESSES_COLLECTION.format(uid=jwt['uid']))
