# 🧠 Git & GitHub Actions – DevOps Notes

This document provides practical, hands-on guidance for using **Git** effectively in software development and for implementing **CI/CD pipelines** using **GitHub Actions**. It is structured for developers and DevOps professionals aiming to build robust workflows and automation.

---

## 🔧 Git: Core Concepts

### 📘 What is Git?

- Git is a **Distributed Version Control System (DVCS)** designed to handle everything from small to very large projects with speed and efficiency.
- Tracks changes in source code, enabling **collaboration**, **rollback**, **version control**, and **branching strategies**.
- Enables developers to work in parallel without overwriting each other’s changes.

---

### 🗂 Local vs Remote Repositories

| Repository Type     | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Local Repository** | The Git repository on a developer's machine. Changes are made and committed locally. |
| **Remote Repository**| Hosted on platforms like GitHub, GitLab, or Bitbucket, allowing team collaboration and CI/CD integration. |

---

### 🔄 Basic Git Workflow

```bash
# Step 1: Stage changes for commit
git add <file>  # Or use '.' to add all changes

# Step 2: Commit staged changes with a message
git commit -m "Descriptive commit message"## 🌳 Git Branching Strategy
```

### 🧪 Why Use Branching?

- Enables **isolated development** of features, bug fixes, or experiments.
- Reduces the risk of breaking the `main` or production codebase.
- Supports **code reviews**, **CI testing**, and **feature toggling**.

---

### 🌱 Common Branching Model

| Branch Name        | Purpose                                  |
|--------------------|-------------------------------------------|
| `main`             | Production-ready code                     |
| `develop`          | Integration branch for feature branches   |
| `feature/<name>`   | New feature development                   |
| `bugfix/<name>`    | Hotfix or issue resolution                |
| `release/<version>`| Pre-release staging                       |
| `hotfix/<issue>`   | Emergency fixes to production             |

```bash
# Create a new feature branch
git checkout -b feature/login-form

# Merge it back to develop after completion
git checkout develop
git merge feature/login-form
```
---

## 🔗 Git Hooks (Automation at Git Events)

### 📎 What Are Git Hooks?

Git hooks are scripts that run automatically when specific Git events occur.

They’re commonly used for:

- ✅ Pre-commit linting  
- 🧹 Code formatting  
- 🔒 Security checks  
- 🧪 Testing enforcement  

---

### 🔍 Common Hooks

| Hook Name     | Triggered On                  | Use Case                            |
|---------------|-------------------------------|-------------------------------------|
| `pre-commit`  | Before a commit is created     | Run tests, format code, lint        |
| `commit-msg`  | After commit message entered   | Enforce commit message standards    |
| `pre-push`    | Before code is pushed          | Run test suite or security checks   |

```bash
# Example pre-commit hook (in .git/hooks/pre-commit)
#!/bin/sh
npm run lint
```

---

## 🚀 GitHub Actions – CI/CD Pipelines

### ⚙️ What Is GitHub Actions?
**GitHub Actions** is a CI/CD platform built into GitHub. It allows you to **automate** workflows and development tasks directly within your repository.
It automates tasks such as:
- 🏗 **Builds**
- ✅ **Tests**
- 🚀 **Deployments**
- 🔔 **Notifications**

> Workflows are defined using **YAML** files inside the `.github/workflows/` directory.

---

### 🏗 Basic Workflow Structure

```yaml
name: Node.js CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: 18

    - run: npm install
    - run: npm test
```

---

## 🧩 Key Components of a GitHub Actions Workflow

| Component | Description                                                  |
|-----------|--------------------------------------------------------------|
| `name`    | Name of the workflow                                         |
| `on`      | Event trigger (e.g., `push`, `pull_request`, `schedule`)     |
| `jobs`    | A set of tasks that run either sequentially or in parallel   |
| `steps`   | Individual commands or actions executed within a job         |

---

## 🔁 Common Use Cases

### 🧪 Continuous Integration (CI)

Automatically run tests on every:

- Pull request (PR)
- Commit to `main` or other branches
- Scheduled intervals (e.g., nightly builds)

### 🚀 Deployment (CD)

Deploy applications to services like:

- **Vercel**
- **Netlify**
- **Heroku**
- **AWS**
- **DigitalOcean**

### 🤖 Automation

Use GitHub Actions to automate tasks such as:

- 🏷 Auto-tagging new releases
- 🔔 Sending Slack or email notifications
- 🔁 Syncing repositories or branches

---

## ✅ Pro Tips for Better Workflows

Make your GitHub Actions pipelines more robust by incorporating:

- 🔐 **Secrets** – Securely store and use API keys, tokens, etc. via GitHub Secrets  
- 💾 **Caching** – Speed up builds by caching dependencies (e.g., npm, pip, yarn)  
- ♻️ **Reusable workflows** – DRY (Don't Repeat Yourself) out logic across projects  
- 🌍 **Environment-specific deploys** – Customize workflows for dev, staging, and production  

