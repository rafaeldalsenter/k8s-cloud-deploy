FROM python:3.8-slim

WORKDIR /app

ENV GOOGLE_APPLICATION_CREDENTIALS='/app/CREDENTIALS.json'

RUN apt-get -y update && apt-get -y install apt-transport-https \
    ca-certificates \
    gnupg \
    curl \
    gnupg-agent \
    software-properties-common

# Terraform install
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && apt-get install terraform

# GCloud install
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && \ 
    apt-get update -y && apt-get install google-cloud-sdk -y

# Kubectl
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update && apt-get install -y kubectl

COPY /cloud_providers /app/cloud_providers
COPY /terraforms /app/terraforms
COPY app.py /app

CMD ["python", "app.py"]