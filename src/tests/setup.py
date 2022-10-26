import json
import os

import pyrebase

pb = pyrebase.initialize_app(json.load(open(os.getenv('FIREBASE_CONFIG'))))


def get_token():
    email = os.getenv('TEST_EMAIL')
    password = os.getenv('TEST_PASS')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        print(jwt)
        return jwt
    except Exception as e:  # pragma: no cover
        print(e)
