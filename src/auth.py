from fastapi import HTTPException
from firebase_admin import auth
from firebase_admin.auth import InvalidIdTokenError


def get_uid(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except InvalidIdTokenError:
        raise HTTPException(401)
    except ValueError:
        raise HTTPException(401)

