from http import client
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text != "<h1>Hello World</h>"
    assert "text/html" in response.headers['content-type']


# def test_post_home():
#     response = client.post("/")
#     assert response.status_code == 200
#     assert "application/json" in response.headers['content-type']
#     assert response.json() == {"hello":"world"}

