from heapq import merge
from firestore import db
from fastapi.responses import JSONResponse

def _get_document(id, collection):
    doc_ref = db.collection(collection).document(id)
    doc = doc_ref.get()
    return doc

def add_document(document, collection):
    doc_ref = db.collection(collection).document(document.id)
    doc = doc_ref.get()
    if doc.exists:
        return JSONResponse(content={"error": f"id {document.id} already exists in collection {collection}."}, status_code=409)
    else:
        data = dict(document)
        del data['id']
        doc_ref.set(data)
        return JSONResponse(content=data, status_code=201)

def find_document(id, collection):
    doc = _get_document(id, collection)
    if doc.exists:
        return JSONResponse(content=doc.to_dict())
    else:
        return JSONResponse(content={"error": f"id {id} was not found."}, status_code=404)

def change_document(id, collection, values):
    doc_ref = db.collection(collection).document(id)
    doc = doc_ref.get()
    if doc.exists:
        current = doc.to_dict()
        new = dict(values)
        non_valid_keys = []
        for key in list(new.keys()):
            if key not in list(current.keys()):
                non_valid_keys.append(key)
        if len(non_valid_keys) > 0:
            return JSONResponse(content={"error": f"key(s) {non_valid_keys} is/are not valid."}, status_code=400)
        updated = {**current, **new}
        doc_ref.set(updated)
        return JSONResponse(content=updated)
    else:
        return JSONResponse(content={"error": f"id {id} was not found."}, status_code=404)