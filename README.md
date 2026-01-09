# 🚀 KubeBridge

KubeBridge is a hands-on Kubernetes platform project that demonstrates how containerized applications are built, deployed, exposed, and continuously managed using real-world DevOps and cloud-native practices.

This project focuses on Kubernetes operations, GitOps automation, and real-world troubleshooting rather than just deploying a demo application.

---

## 🔧 Tech Stack

- Docker
- Kubernetes (Google Kubernetes Engine – GKE)
- Terraform (Infrastructure as Code)
- Argo CD (GitOps Continuous Deployment)
- Google Artifact Registry
- Python (Flask)
- kubectl & gcloud CLI
- GitHub (SSH-based authentication)

---

## 📦 Project Overview

KubeBridge simulates a real production Kubernetes platform.

The project includes:
- Infrastructure provisioning using Terraform
- A containerized Python web application
- Image storage in Google Artifact Registry
- Kubernetes Deployment and Service objects
- Liveness and readiness probes
- GitOps-based Continuous Deployment using Argo CD
- Hands-on debugging of Docker, Kubernetes, and IAM issues

---

## 📁 Repository Structure

app/
infra/
k8s/
Dockerfile
README.md

yaml
Copy code

---

## 🔁 CI/CD

This repository includes a GitHub Actions CI pipeline that automatically:
- Lints Python code using `ruff`
- Validates Kubernetes manifests using `kubeconform`
- Builds the Docker image to catch Dockerfile issues early

The pipeline runs on every push to `main` and on pull requests.

---

## 🚀 GitOps Continuous Deployment

KubeBridge uses GitOps-style Continuous Deployment with Argo CD.

- Argo CD continuously watches the `main` branch and `k8s/` directory
- Any change pushed to Git is automatically synced to the Kubernetes cluster
- Auto-sync, self-healing, and pruning keep the cluster consistent with Git

---

## ✅ Verification

- Terraform plan reports no drift
- Application pods run successfully in GKE
- Application is accessible via Kubernetes Service
- Changes are deployed via GitOps without manual `kubectl apply`

---

## 📌 Resume Highlights

- Built a production-grade Kubernetes platform on GCP using Terraform
- Implemented GitOps Continuous Deployment with Argo CD
- Published and deployed Docker images via Artifact Registry
- Debugged real Kubernetes, Docker, and IAM permission issues end-to-end

## 👤 End Credits

Built and maintained by **Rithika Reddy** as a hands-on DevOps and Kubernetes learning project.

This project was designed to simulate real-world cloud-native workflows, including infrastructure provisioning, containerization, GitOps-based deployments, and operational troubleshooting.

All infrastructure and application components were built, deployed, debugged, and documented end-to-end.

