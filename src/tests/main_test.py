import os

from fastapi.testclient import TestClient

from main import app
from tests.setup import get_token

client = TestClient(app)


def test_root_without_auth():
    response = client.get("/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Bearer authentication is needed"}


def test_root():
    headers = {"Authorization": f"Bearer {get_token()}"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {os.getenv('TEST_EMAIL')}"}
