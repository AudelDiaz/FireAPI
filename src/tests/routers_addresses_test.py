from fastapi.testclient import TestClient

from main import app
from tests.setup import get_token

client = TestClient(app)
TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def test_create_address_account():
    body = {
        "name": "Test Address",
        "address": "Test 123",
        "city_id": "24534234",
        "postal_code": "111111"
    }
    response = client.post("/api/v1/account/addresses", json=body, headers=HEADERS)
    assert response.status_code == 201


def test_get_addresses():
    response = client.get("/api/v1/account/addresses", headers=HEADERS)
    assert response.status_code == 200


def test_get_addresses_by_id():
    response_addresses = client.get("/api/v1/account/addresses", headers=HEADERS)
    addresses = response_addresses.json()['addresses']
    address_id = list(addresses[0].keys())[0]
    response = client.get(f"/api/v1/account/addresses/{address_id}", headers=HEADERS)
    assert response.status_code == 200

    response = client.get("/api/v1/account/addresses/abcd", headers=HEADERS)
    assert response.status_code == 404


def test_update_address_account():
    body = {
        "name": "Update address name"
    }
    response_addresses = client.get("/api/v1/account/addresses", headers=HEADERS)
    addresses = response_addresses.json()['addresses']
    address_id = list(addresses[0].keys())[0]
    response = client.patch(f"/api/v1/account/addresses/{address_id}", json=body, headers=HEADERS)
    assert response.status_code == 200

    response = client.patch("/api/v1/account/addresses/abcd", json=body, headers=HEADERS)
    assert response.status_code == 404

    body = {
        "whatever": "Invalid field"
    }
    response = client.patch(f"/api/v1/account/addresses/{address_id}", json=body, headers=HEADERS)
    assert response.status_code == 400


def test_delete_addresses_by_id():
    response_addresses = client.get("/api/v1/account/addresses", headers=HEADERS)
    addresses = response_addresses.json()['addresses']
    address_id = list(addresses[0].keys())[0]
    response = client.delete(f"/api/v1/account/addresses/{address_id}", headers=HEADERS)
    assert response.status_code == 200

    response = client.delete(f"/api/v1/account/addresses/{address_id}", headers=HEADERS)
    assert response.status_code == 404
