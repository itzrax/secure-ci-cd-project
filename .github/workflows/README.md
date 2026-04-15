# Secure CI/CD DevSecOps Project

##  Project Title
Automated Security Compliance Checks in CI/CD Pipeline

---

##  Problem Statement
Manual security checks in software development are slow, inconsistent, and error-prone, leading to insecure deployments.

---

##  Solution
This project implements a DevSecOps pipeline that automates security checks using GitHub Actions, Bandit, and Trivy to detect vulnerabilities early in the development lifecycle.

---

##  Tools & Technologies
- Python (Flask)
- Docker
- GitHub Actions (CI/CD)
- Bandit (Static Code Analysis)
- Trivy (Container Security Scanning)

---

##  Workflow / Architecture

1. Developer pushes code to GitHub  
2. GitHub Actions triggers CI/CD pipeline  
3. Bandit scans Python code for vulnerabilities  
4. Docker image is built  
5. Trivy scans Docker image for security issues  
6. Pipeline passes or fails based on security results  

---

##  Screenshots

###  Successful Pipeline
![Success](screenshots/success.png)

###  Failed Pipeline
![Failure](screenshots/failure.png)

###  Trivy Security Scan
![Trivy](screenshots/trivy.png)

---

##  Key Features
- Automated security checks in CI/CD
- Early vulnerability detection
- Docker image security scanning
- Fail-fast pipeline for insecure code

---

## ▶ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py