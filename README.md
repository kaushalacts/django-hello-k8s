# Django Hello World on Kubernetes 🚀

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5.svg)](https://kubernetes.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-yellow.svg)](https://www.python.org/)

A production-ready Django "Hello World" application demonstrating modern DevOps practices with Docker containerization and Kubernetes deployment. This project serves as a foundation for building scalable web applications in cloud-native environments.

## ✨ Features

- **Dynamic Hello World**: Displays greeting with server timestamp and pod hostname
- **Container-Ready**: Lightweight Docker image based on `python:3.12-slim`
- **Kubernetes Native**: Production-ready manifests for deployment and service
- **Horizontally Scalable**: Easy scaling with Kubernetes replicas
- **Cloud Agnostic**: Works on any Kubernetes cluster (Minikube, EKS, GKE, AKS)
- **DevOps Ready**: Perfect foundation for CI/CD pipelines

## 📂 Project Structure

```
hello-world/
├── Dockerfile                    # Container configuration
├── requirements.txt              # Python dependencies                
├── hello-world/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hello/                       # Main Django app
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
├── k8s-manifests/               # Kubernetes deployment files
│   ├── hello-world-deployment.yaml
│   └── hello-world-service.yaml
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes cluster (Minikube for local development)
- kubectl CLI tool

### 1. Local Development (Without Docker)

```bash
# Clone the repository
git clone <https://github.com/kaushalacts/django-hello-k8s.git>
cd hello-world

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Django development server
python hello-world.py runserver 0.0.0.0:8000
```

**🌐 Access**: http://127.0.0.1:8000

### 2. Docker Deployment

```bash
# Build Docker image
docker build -t hello-world:v1 .

# Run container
docker run -p 8000:8000 hello-world:v1
```

**🌐 Access**: http://localhost:8000

### 3. Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s-manifests/hello-deployment.yaml
kubectl apply -f k8s-manifests/hello-service.yaml

# Verify deployment
kubectl get pods -l app=hello-world
kubectl get svc hello-service

# For Minikube users - expose service
minikube service hello-service
```

**🌐 Access**: Use the URL provided by Minikube service command

## 📊 Monitoring & Management

### Check Application Status

```bash
# View pods
kubectl get pods -l app=hello-world

# Check pod logs
kubectl logs -l app=hello-world

# Describe deployment
kubectl describe deployment hello-deployment
```

### Scaling Your Application

```bash
# Scale to 5 replicas
kubectl scale deployment hello-world-deployment --replicas=5

# Verify scaling
kubectl get pods -l app=hello-world

# View deployment status
kubectl rollout status deployment hello-deployment
```

### Service Discovery

```bash
# Get service details
kubectl describe svc hello-service

# Port forwarding (alternative access method)
kubectl port-forward svc/hello-service 8080:8000
```

## 🐳 Docker Configuration

The Dockerfile uses multi-stage optimization principles:

- **Base Image**: `python:3.9-slim` for minimal footprint
- **Security**: Non-root user execution
- **Performance**: Optimized layer caching
## ☸️ Kubernetes Architecture

### Deployment Features
- **Replicas**: 2 pods by default (configurable)
- **Rolling Updates**: Zero-downtime deployments
- **Resource Limits**: Memory and CPU constraints
- **Health Checks**: Readiness and liveness probes
- **Labels**: Proper labeling for service discovery

### Service Configuration
- **Type**: NodePort (easily changeable to LoadBalancer/ClusterIP)
- **Port Mapping**: 8000 (container) → 30000 (node)
- **Load Balancing**: Automatic traffic distribution across pods

## 🔧 Configuration

### Environment Variables

The application accepts these environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DJANGO_DEBUG` | `False` | Enable Django debug mode |
| `DJANGO_SECRET_KEY` | Generated | Django secret key |
| `PORT` | `8000` | Application port |

### Kubernetes Customization

Edit the manifest files to customize:

- **Replicas**: Change `replicas` in deployment.yaml
- **Resources**: Modify `resources.limits` and `resources.requests`
- **Service Type**: Change `type` in service.yaml (NodePort/LoadBalancer/ClusterIP)
- **Environment**: Add environment variables to deployment spec

## 🌍 Cloud Deployment

### AWS EKS
```bash
# Configure kubectl for EKS
aws eks update-kubeconfig --region us-west-2 --name your-cluster-name

# Deploy
kubectl apply -f k8s-manifests/
```

### Google GKE
```bash
# Configure kubectl for GKE
gcloud container clusters get-credentials your-cluster-name --zone us-central1-a

# Deploy
kubectl apply -f k8s-manifests/
```

### Azure AKS
```bash
# Configure kubectl for AKS
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster

# Deploy
kubectl apply -f k8s-manifests/
```

## 🛠️ Development Workflow

### Making Changes

1. **Update Code**: Modify Django application
2. **Build Image**: `docker build -t hello-world:v2 .`
3. **Update Deployment**: `kubectl set image deployment/hello-world-deployment hello-world=hello-world:v2`
4. **Monitor Rollout**: `kubectl rollout status deployment/hello-world-deployment`

### Testing

```bash
# Run Django tests
python hello-world.py test

# Test Docker build
docker build -t hello-world:test .
docker run --rm hello-world:test python hello-world.py test
```

 
## 🐛 Troubleshooting

### Common Issues

**Pod not starting:**
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

**Service not accessible:**
```bash
kubectl describe svc hello-service
kubectl get endpoints hello-service
```

**Image pull issues:**
```bash
# Check image name in deployment
kubectl get deployment hello-deployment -o yaml
```

 

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit changes: `git commit -am 'Add feature'`
5. Push to branch: `git push origin feature-name`
6. Submit a Pull Request

 

 

⭐ Star this repository if you found it helpful!

 

*Built with ❤️ for the DevOps and Python communities*
