# Bus Failure Prediction – End-to-End MLOps System

This project builds a complete MLOps pipeline for predicting bus component failures.  
It includes model training, an inference API, Docker packaging, CI testing, and Kubernetes deployment.

---

##  Project Overview

This system predicts equipment failures using sensor-like features such as temperature, vibration, mileage, and load.

The project demonstrates a full production-style workflow:

- Data generation and ML model training (scikit-learn)
- Preprocessing + model pipeline saved with joblib
- FastAPI inference service (`/predict`)
- Docker containerization
- GitHub Actions CI (pytest + Docker build)
- Kubernetes Deployment + Service (Minikube)

---

## Model Input Example

```json
{
  "temperature_mean_last_24h": 80,
  "vibration_level": 3.2,
  "mileage_km": 250000,
  "engine_load": 60,
  "ambient_temp": 12,
  "coolant_pressure": 1.4,
  "battery_voltage": 24.5
}
