import sys
import os

# Add project root to sys.path so 'app' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict_endpoint():
    sample_input = {
        "features": {
            "aa_000": 0.0,
            "ab_000": 1.0,
            "ac_000": 0.5
        }
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200

    data = response.json()

    assert "failure_prediction" in data
    assert "failure_probability" in data
    assert isinstance(data["failure_prediction"], int)
    assert isinstance(data["failure_probability"], float)
