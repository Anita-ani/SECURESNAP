# SECURESNAP

 A secure FastAPI application with a full DevSecOps pipeline including GitHub Actions, Jenkins, Bandit, ZAP, and AWS deployment.

## Features
- FastAPI backend
- HTML frontend
- Dockerized
- CI/CD with GitHub Actions + Jenkins
- Security Scanning (Bandit, ZAP)
- Deployable to AWS

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
