import os
from cloud_providers.gcp import Gcp

def get_cloud_provider():
    cloud_env = os.getenv('CLOUD')

    if(cloud_env == 'gcp'):
        return Gcp()

    raise Exception(f"The CLOUD environment variable (value: {cloud_env}) is not implemented")

cloud_provider = get_cloud_provider()

cloud_provider.configure()
cloud_provider.terraform_apply()
cloud_provider.kubernetes_apply(".")

print('\033[92mSuccess :)')



