from fastapi.testclient import TestClient

from main import app
from tests.setup import get_token

client = TestClient(app)
TOKEN = get_token()


def test_get_account():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = client.get("/api/v1/account", headers=headers)
    assert response.status_code == 200


def test_create_account_account():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    body = {
        "first_name": "Audel",
        "last_name": "Diaz"
    }
    response = client.post("/api/v1/account", json=body, headers=headers)
    assert response.status_code == 409


def test_update_account_account():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    body = {
        "email": "hola@audeldiaz.work"
    }
    response = client.patch("/api/v1/account", json=body, headers=headers)
    assert response.status_code == 200
