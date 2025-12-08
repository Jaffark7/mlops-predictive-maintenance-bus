APS Failure Prediction – End-to-End MLOps System

This project builds a complete MLOps pipeline for predicting failures in Scania’s Air Pressure System (APS).
It covers the entire machine learning lifecycle: model development, serving, testing, containerization, and Kubernetes deployment.

Project Overview

The goal of the system is to detect early signs of APS component failure using ~170 anonymized sensor features.
The project demonstrates a realistic production-style workflow using modern MLOps tools:

Data preprocessing and model training (Scikit-Learn + XGBoost)

Full ML pipeline saved with joblib

FastAPI inference API (/predict)

Automated API testing with pytest

Docker containerization

Kubernetes Deployment + Service (Minikube)

The purpose of the project is to learn and demonstrate how a real-world machine learning model transitions from development to production, and to help others understand the fundamentals of deploying ML systems.

Model Input Example

Predictions are made by submitting a dictionary of APS feature values:

{
  "features": {
    "aa_000": 0.5,
    "ab_000": 1.0,
    "ac_000": 0.3
  }
}


The model automatically handles missing features through its preprocessing pipeline.
