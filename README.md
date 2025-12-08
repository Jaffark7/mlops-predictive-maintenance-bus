# APS Failure Prediction – End-to-End MLOps System

A complete MLOps pipeline for predicting failures in Scania's Air Pressure System (APS), demonstrating the full machine learning lifecycle from development to production deployment.

---

## Project Overview

This system detects early signs of APS component failure using approximately 170 anonymized sensor features. The project showcases a realistic production-style workflow using modern MLOps tools and best practices.

### What This Project Demonstrates

- End-to-end machine learning pipeline implementation
- Production-ready API development and testing
- Containerization and orchestration fundamentals
- Real-world MLOps workflow from development to deployment

---

## Architecture

The system consists of the following components:

### Data & Model Development
- **Preprocessing & Training**: Scikit-Learn + XGBoost
- **Pipeline Serialization**: Joblib for complete ML pipeline persistence

### API & Testing
- **Inference API**: FastAPI with `/predict` endpoint
- **Automated Testing**: Pytest for API validation

### Deployment
- **Containerization**: Docker for reproducible environments
- **Orchestration**: Kubernetes Deployment + Service (Minikube)

---

## Model Input Format

Predictions are made by submitting a JSON payload with APS feature values:
```json
{
  "features": {
    "aa_000": 0.5,
    "ab_000": 1.0,
    "ac_000": 0.3
  }
}
```

> **Note**: The model automatically handles missing features through its preprocessing pipeline.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- Minikube (for local Kubernetes deployment)

### Installation

1. Clone the repository
```bash
   git clone 
   cd aps-failure-prediction
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run the API locally
```bash
   uvicorn main:app --reload
```

4. Test the API
```bash
   pytest tests/
```

---

## Docker Deployment

Build and run the container:
```bash
docker build -t aps-prediction-api .
docker run -p 8000:8000 aps-prediction-api
```

---

## Kubernetes Deployment

Deploy to Minikube:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Access the service:
```bash
minikube service aps-prediction-service
```

---

## API Usage

### Health Check
```bash
curl http://localhost:8000/health
```

### Make Prediction
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "features": {
      "aa_000": 0.5,
      "ab_000": 1.0,
      "ac_000": 0.3
    }
  }'
```

---

## Project Structure
```
aps-failure-prediction/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── pipeline.joblib
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
├── api/
│   └── main.py
├── tests/
│   └── test_api.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Learning Objectives

This project serves as a practical guide for understanding:

- How machine learning models transition from development to production
- MLOps fundamentals and best practices
- API design for ML inference services
- Container orchestration with Kubernetes

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
## License

[Your License Here]

---

## Acknowledgments

- Dataset provided by Scania AB
- Built as a demonstration of MLOps principles and practices

---

## Contact

www.linkedin.com/in/jaffarkamil

