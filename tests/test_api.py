from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    sample_input = {
        "temperature_mean_last_24h": 80,
        "vibration_level": 3.2,
        "mileage_km": 250000,
        "engine_load": 60,
        "ambient_temp": 12,
        "coolant_pressure": 1.4,
        "battery_voltage": 24.5
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200

    data = response.json()
    assert "failure_prediction" in data
    assert "failure_probability" in data
    assert isinstance(data["failure_prediction"], int)
    assert isinstance(data["failure_probability"], float)
