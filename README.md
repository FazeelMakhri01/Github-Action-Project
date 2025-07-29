# 🌦️ Weather CLI App

A minimal yet powerful Python-based CLI app that fetches the current weather for any city using the public API from [wttr.in](https://wttr.in).
This project is a hands-on demonstration of modern DevOps practices, including containerization with Docker and CI/CD automation using GitHub Actions. Built for simplicity, reliability, and scalability.

---

## 🚀 Features

- 🐍 Lightweight Python CLI tool (no external dependencies)
- 🐳 Fully containerized with a slim Docker base image (`python:3.9-slim`)
- 🔁 CI/CD pipeline powered by **GitHub Actions**
- 🔐 Secure Docker Hub deployment using **GitHub Secrets**
- 🏷️ Versioned Docker images tagged with Git commit SHA (short)
- 📦 Production-ready workflow following DevOps CI/CD standards

---

## 🧪 Local Usage

Run the CLI app directly via Python:

```bash
python app.py <city>
# Example
python app.py London
```

---

🐳 Docker Usage
Build Locally:
```bash
docker build -t weather-cli-app .
```

Run Container:
```bash
docker run weather-cli-app London
```

---

## 🔄 GitHub Actions CI/CD Workflow
On every push to the main branch:

- ✅ Code Inspection using flake8 and pylint
- 🛠 Builds Docker image
- 🏷 Tags the image with the first 7 characters of the Git commit SHA
- 📦 Pushes the image to Docker Hub
- 🚀 (Optional) Deploys to AWS EC2 (via SSH, SCP, or ECS depending on configuration)

GitHub Secrets Used
- DOCKER_USERNAME
- DOCKER_PASSWORD
- (Optional) EC2_HOST, EC2_USER, EC2_KEY for deployment

---

## 🧩 Project Structure
```bash
weather-cli-app/
├── app.py                  # CLI Application
├── Dockerfile              # Docker build instructions
├── .github/
│   └── workflows/
│       └── main.yml          # GitHub Actions CI/CD pipeline
├── .gitignore
└── README.md               # Project documentation
```

---




