# Web Crawler API
## Description
This is a lightweight web crawler service built using Flask. It crawls a given URL, generates a sitemap of the links, and returns it in a tree structure. The crawler is restricted to a single domain to avoid following external links. This project includes Dockerization for easy deployment and a Kubernetes configuration for cloud deployment.

### Features
- **Crawl URL**: Crawls a given URL and generates a sitemap.
- **Domain Restriction**: Crawls only internal links within the provided domain.
- **Health Check**: /health endpoint to monitor the status of the service.
- **Dockerized**: Runs inside a Docker container for easy deployment.
- **Kubernetes-ready**: Configured for deployment on Kubernetes.

---

## Tools Required
Before proceeding with any of the setups, ensure you have the following tools installed:

- Docker (for containerization and testing)
- Kubernetes & kubectl (for deploying to Kubernetes)
- Minikube (for local Kubernetes testing)
- Python 3.8+ installed (for local testing).

---

## Local Setup
### 1. Clone the Repository
- Clone the repository to your local machine:
```bash
git clone https://github.com/PrakharGupta2001/web_crawler.git
cd web_crawler
```

### 2. Install Dependencies
Create a virtual environment (optional but recommended) and install the required Python packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Running the Application Locally
To run the Flask application locally:
```bash
python app/routes.py
```
The Flask server will be running at http://localhost:5000.
You can access the **/crawl** and **/health** endpoints to test the functionality.

---

## Docker Setup

### 1. Install Docker
Ensure that Docker is installed on your machine.

### 2. Build the Docker Image
To pull the Docker image of the web crawler:
```bash
docker pull prakhargupta05/web_crawler:02
```

### 3. Run the Docker Container
To run the web crawler inside a Docker container:
```bash
docker run -d -p 5000:5000 prakhargupta05/web_crawler:02
```
This will expose the Flask application on http://localhost:5000.

---

## Kubernetes Deployment

### 1. Pre-requisites for Kubernetes
Make sure you have Minikube and kubectl installed on your system:

Install Minikube
Install kubectl
Start Minikube (for local Kubernetes testing):

```bash
Copy code
minikube start
```

### 2. Apply the Kubernetes Resources
Apply the deployment, service, and ingress to your Kubernetes cluster:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

### 3. Verify the Deployment
Check the pods:
```bash
kubectl get pods
```
Check the service:
```bash
kubectl get services
```
Check the ingress:
```bash
kubectl get ingress
```
### 4. Access the Application
If you're using Minikube, you can access the application via the following command:
```bash
minikube service web-crawler-service
```
If you’re using a LoadBalancer, you can access the app via the external IP provided by Kubernetes.

For local development, if you use web-crawler.local, make sure to add it to your /etc/hosts or Windows hosts file to route traffic to 127.0.0.1.

Conclusion
You now have a fully functional web crawler that can be run locally, in Docker, or on Kubernetes. This setup ensures scalability, monitoring, and easy deployment across different environments.
