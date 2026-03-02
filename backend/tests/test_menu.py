from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_menu_items():
    response = client.get("/menu")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) >= 2

    burger = next(i for i in data["items"] if i["id"] == 1)
    assert burger["name"] == "Veg Grilled Paneer Burger"
    assert burger["price"] == 4.0

    combo = next(i for i in data["items"] if i["id"] == 2)
    assert combo["price"] == 10.0
