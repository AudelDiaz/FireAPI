from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from firestore import db


def find_document(document_id, collection):
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    return doc, doc_ref


def add_document(document_id, document, collection):
    doc, doc_ref = find_document(document_id, collection)
    if doc.exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"document_id {document_id} already exists in collection {collection}.",
            headers=None,
        )
    else:
        data = dict(document)
        doc_ref.set(data)
        return JSONResponse(content=data, status_code=201)


def get_document(document_id, collection):
    doc, _doc_ref = find_document(document_id, collection)
    if doc.exists:
        return JSONResponse(content=doc.to_dict())
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"document_id {document_id} was not found.",
            headers=None,
        )


def change_document(document_id, collection, values):
    doc, doc_ref = find_document(document_id, collection)
    if doc.exists:
        current = doc.to_dict()
        new = dict(values)
        non_valid_keys = []
        for key in list(new.keys()):
            if key not in list(current.keys()):
                non_valid_keys.append(key)
        if len(non_valid_keys) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"key(s) {non_valid_keys} is/are not valid.",
                headers=None,
            )
        updated = {**current, **new}
        doc_ref.set(updated)
        return JSONResponse(content=updated)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"document_id {document_id} was not found.",
            headers=None,
        )
