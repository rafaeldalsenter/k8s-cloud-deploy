# k8s-cloud-deploy
🚢 GCP Kubernetes deployment

Application that creates and configures K8s cloud environment:
- Configures the GCP by enabling the necessary resources.
- Execute Terraform scripts.
- Execute K8s scripts. 

Prerequisites:
- K8s files.
- CREDENTIALS.json, created by [service account](https://cloud.google.com/iam/docs/service-accounts) key from GCP.

This image must be used as an "image-base" to generate a new image containing the prerequisite files.

Example of use:

```dockerfile
FROM rafaeldalsenter/k8s-cloud-deploy

ENV PROJECT_ID=test-project
ENV REGION=us-west1
ENV CLOUD=gcp

COPY . ./
```
