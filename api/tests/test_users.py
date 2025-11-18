from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/", json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["username"] == "testuser"
