# 🚀 DockPulse – Container Health Monitoring System

DockPulse is a real-time container monitoring solution designed to monitor Docker containers and visualize their health and performance metrics through an interactive web dashboard.

This repository contains two implementations of the project:

- **Version 1 (V1)** – Python Flask Implementation
- **Version 2 (V2)** – Node.js Implementation

---

## 📖 Project Overview

Modern DevOps environments rely heavily on containerized applications. Monitoring container health is essential to ensure application reliability, efficient resource utilization, and quick issue detection.

DockPulse provides:

- Real-time container monitoring
- CPU usage tracking
- Memory usage monitoring
- Container status visualization
- Health classification
- Responsive dashboard
- Docker integration
- CI/CD support using Jenkins

---

# 📂 Repository Structure

```text
DockPulse/
│
├── V1-Flask/
│   ├── app.py
│   ├── monitor.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── Jenkinsfile
│   ├── templates/
│   └── static/
│
├── V2-NodeJS/
│   ├── server.js
│   ├── package.json
│   ├── Dockerfile
│   ├── Jenkinsfile
│   └── node_modules/
│
└── README.md
```

---

# 🔹 Version 1 – Flask Implementation

### Technologies Used

- Python
- Flask
- Docker
- HTML
- CSS
- Bootstrap
- JavaScript
- Jenkins

### Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

# 🔹 Version 2 – Node.js Implementation

### Technologies Used

- Node.js
- Express.js
- Docker
- HTML
- CSS
- JavaScript
- Jenkins

### Run Locally

Install dependencies:

```bash
npm install
```

Start the application:

```bash
npm start
```

Open:

```text
http://localhost:5000
```

---

# 🐳 Docker Deployment

Build Docker Image:

```bash
docker build -t dockpulse .
```

Run Container:

```bash
docker run -p 5000:5000 dockpulse
```

---

# ⚙️ CI/CD Integration

Both versions include a Jenkins pipeline for:

- Source Code Checkout
- Build Automation
- Container Creation
- Deployment Automation

---

# 📊 Features

- Real-time Docker container monitoring
- CPU and memory utilization tracking
- Container health status classification
- Automatic dashboard refresh
- Responsive user interface
- Dockerized deployment
- Jenkins CI/CD integration

---

# 🔮 Future Enhancements

- Email notifications
- Alert management
- Kubernetes integration
- Log monitoring
- Historical data storage
- Grafana integration
- Predictive analytics using AI/ML

---

# 🎯 Use Cases

- DevOps Monitoring
- Docker Environment Management
- Resource Utilization Analysis
- Infrastructure Monitoring
- Educational Demonstrations

---

# 👩‍💻 Author

**B Hasini**

Container Health Monitoring System – DevOps Mini Project
