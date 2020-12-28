# k8s-cloud-deploy
🚢 GCP Kubernetes deployment

This application creates and configures K8s cloud environment:
- Configures the GCP by enabling the necessary resources.
- Execute Terraform scripts.
- Execute K8s scripts. 

Prerequisites:
- K8s files (*.yaml).
- CREDENTIALS.json, created by [service account](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.213572756.1215753345.1606170525-486567454.1606170525) key from GCP.

This image must be used as an "image-base" to generate a new image containing the prerequisite files.

Example of use:

```dockerfile
FROM rafaeldalsenter/k8s-cloud-deploy:1.0

ENV PROJECT_ID=test-project
ENV REGION=us-west1
ENV CLOUD=gcp

# This "." folder contains K8s files and CREDENTIALS.json
COPY . /app
```
