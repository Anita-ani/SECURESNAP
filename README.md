#  SECURESNAP: Secure CI/CD Pipeline with Jenkins + GitHub + Prometheus + Grafana

## Overview

SECURESNAP is a DevSecOps pipeline that integrates Jenkins, GitHub, SonarQube, Prometheus, and Grafana to enforce security, quality, and observability in every code delivery process.

##  What This Setup Achieves

*  Secure CI/CD pipeline with GitHub + Jenkins
*  Static Application Security Testing (SAST) using SonarQube
*  Quality Gate enforcement
* GitHub secrets and credential management
*  Prometheus & Grafana for monitoring Jenkins
*  Docker-based isolated builds

---

##  Architecture Diagram

This diagram shows:

* Jenkins master with Docker agents
* SonarQube connected to Jenkins
* GitHub as the source repository
* Prometheus scraping Jenkins metrics
* Grafana dashboarding Prometheus 



##  Step-by-Step Setup

### 1. Prerequisites

* Docker & Docker Compose installed
* GitHub repository with pipeline code
* Jenkins and SonarQube images (official)
* Prometheus and Grafana Docker images

### 2.  Clone Repo & Configure Credentials

```bash
git clone https://github.com/Anita-ani/SECURESNAP.git
cd SECURESNAP
```

Configure GitHub credentials as Jenkins secrets.

### 3.  Run Jenkins, SonarQube, Prometheus, and Grafana

```bash
docker-compose up -d
```

### 4.  Connect Jenkins to GitHub

* Install GitHub and Docker plugins
* Add GitHub credentials (personal access token)
* Configure webhook in GitHub

### 5.  Setup Jenkins Pipeline

* Use the provided `Jenkinsfile`
* Add SonarQube scanner in Jenkins global tools
* Configure Quality Gate

### 6.  Include SonarQube in Pipeline

```groovy
stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            sh 'sonar-scanner'
        }
    }
}
```

### 7.  Setup Prometheus to Scrape Jenkins

Update `prometheus.yml`:

```yaml
  - job_name: 'jenkins'
    metrics_path: '/prometheus'
    static_configs:
      - targets: ['jenkins:8080']
```

### 8.  Setup Grafana

* Access Grafana at `http://localhost:3000`
* Add Prometheus as data source
* Import FastAPI Jenkins Dashboard using ID `13666`

---

##  Security Enhancements

* Read-only Docker mounts
* GitHub secrets for API keys and tokens
* SonarQube for SAST and code smells
* Jenkins access controls

---

##  Screenshots

1. Jenkins Dashboard 
2. SonarQube Analysis 
3. Prometheus Target 
4. Grafana CI/CD Dashboard 
   

##  Common Errors & Fixes

| Error                           | Fix                                           |
| ------------------------------- | --------------------------------------------- |
| Jenkins build fails             | Check GitHub credentials or webhook setup     |
| Prometheus can't scrape Jenkins | Verify target IP & port mapping               |
| Grafana shows no data           | Check Prometheus data source and dashboard ID |

---

##  How to Run the Pipeline

1. Push code to GitHub
2. GitHub triggers Jenkins webhook
3. Jenkins pulls, builds, and runs SAST via SonarQube
4. Prometheus scrapes Jenkins metrics
5. Grafana displays real-time CI/CD performance

---

##  Final Notes & Thanks

This project demonstrates a secure and observable CI/CD pipeline with GitHub, Jenkins, and monitoring using Prometheus and Grafana — all aligned with modern DevSecOps practices like SAST, quality gates, and pipeline security.

**Thanks for reviewing this setup!** Feel free to fork, extend, or contribute.
