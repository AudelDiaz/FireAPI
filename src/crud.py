from firestore import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def add_user(user):
    doc_ref = db.collection('users').document(user.uid)
    doc = doc_ref.get()
    if doc.exists:
        return JSONResponse(content={"error": f"username {user.uid} already exists."}, status_code=409)
    else:
        doc_ref.set({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        return JSONResponse(content=jsonable_encoder(user), status_code=200)