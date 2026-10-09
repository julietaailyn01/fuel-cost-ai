from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_home():
    response= client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_predict():
    response = client.post(
        "/predict",
        json = {
            "distance_km": 250,
            "fuel_price_per_liter": 1500,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["distance_km"] ==250
    assert data["fuel_price_per_liter"] ==1500
    assert data["predicted_liters"] > 0
    assert data["estimated_cost"] > 0

def test_predict_invalid_distance():
    response= client.post(
        "/predict",
        json={
            "distance_km": -100,
            "fuel_price_per_liter": 1500
        }
    )

    assert response.status_code ==422


def test_predict_invalid_fuel_price():
    response =client.post(
        "/predict",
        json = {
            "distance_km": 250,
            "fuel_price_per_liter" : 0,
        }
    )
    assert response.status_code == 422