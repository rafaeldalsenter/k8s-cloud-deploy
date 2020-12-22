import os
import subprocess
from cloud_providers.cloud_provider import CloudProvider

class Gcp(CloudProvider):

    def __init__(self):
        self.__id_project = os.getenv('PROJECT_ID')
        self.__region = os.getenv('REGION')
        self.__key_file = os.getenv('CREDENTIALS_FILE', '/app/CREDENTIALS.json')
        self.__terraform_dir = './terraforms/gcp'

        if(self.__id_project == None or self.__region == None):
            raise Exception("Set the PROJECT_ID and REGION environment variables")

    def configure(self):
        subprocess.run(["gcloud", "config", "set", "project", self.__id_project], check=True)
        subprocess.run(["gcloud", "auth", "activate-service-account", "--key-file", self.__key_file], check=True)
        subprocess.run(["gcloud", "services", "enable", "compute.googleapis.com"], check=True)
        subprocess.run(["gcloud", "services", "enable", "container.googleapis.com"], check=True)

    def terraform_apply(self):
        subprocess.run(["terraform", "init"], cwd=self.__terraform_dir)
        subprocess.run(["terraform", "apply", "-var", "project_id=%s" % self.__id_project, "-var", "region=%s" % self.__region, "-auto-approve"],
            cwd=self.__terraform_dir)

    def kubernetes_apply(self, dir):
        subprocess.run(["gcloud", "container", "clusters", "get-credentials", "%s-gke" % self.__id_project, "--region", "%s" % self.__region, "--project", "%s" % self.__id_project])
        subprocess.run(["kubectl", "apply", "-f", dir, "--recursive"])