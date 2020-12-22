# k8s-cloud-deploy
🚢 GCP Kubernetes deployment

A Docker image with install, configure gcloud and apply terraform and Kubernetes deployment files.

Para GCP:
docker run --env PROJECT_ID=teste-multicloud --env REGION=us-west1 --env CLOUD=gcp rafaeldalsenter/k8s-multicloud-deploy
