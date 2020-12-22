# k8s-cloud-deploy
🚢 GCP Kubernetes deployment

Application that creates and configures K8s cloud environment:
- Configures the GCP by enabling the necessary resources.
- Execute Terraform scripts.
- Execute K8s scripts. 

Prerequisites:
- K8s files.
- CREDENTIALS.json, created by service acconunt key from GCP.


Para GCP:
docker run --env PROJECT_ID=teste-multicloud --env REGION=us-west1 --env CLOUD=gcp rafaeldalsenter/k8s-multicloud-deploy
