# KubeBridge 🚀

KubeBridge is a hands-on Kubernetes platform project that demonstrates how containerized applications are deployed, exposed, and managed using real-world DevOps and cloud-native practices.

This project focuses on understanding **Kubernetes networking, ingress traffic flow, and operational troubleshooting**, rather than just deploying a demo app.

---

## 🔧 Tech Stack

- Docker
- Kubernetes (Minikube)
- NGINX Ingress Controller
- Python (Flask)
- GitHub (SSH-based authentication)

---

## 📦 Project Overview

KubeBridge simulates how a real production service is exposed and managed in Kubernetes.

The project includes:
- A containerized Python web application
- Kubernetes Deployment and Service objects
- NGINX Ingress for external traffic routing
- Custom domain-based routing
- Hands-on debugging of Docker, Minikube, and Kubernetes issues

## 🔁 CI/CD

This repository includes a GitHub Actions CI pipeline that automatically:
- Lints Python code using `ruff`
- Validates Kubernetes manifests using `kubeconform`
- Builds the Docker image to catch Dockerfile issues early

The pipeline runs on every push to `main` and on pull requests.

## 🚀 CD Automation (GitOps)

KubeBridge uses GitOps-style Continuous Deployment with Argo CD.

- Argo CD continuously watches the `main` branch and the `k8s/` directory
- Any change pushed to Git is automatically synced to the Kubernetes cluster
- Auto-sync, self-healing, and pruning keep the cluster consistent with Git

---
