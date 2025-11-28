from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CI/CD Python App Running!"}

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from CI/CD!"}

