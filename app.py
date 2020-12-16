import os
from cloud_providers.gcp import Gcp
from cloud_providers.azure import Azure
from cloud_providers.aws import Aws

def get_cloud_provider():
    cloud_env = os.getenv('CLOUD')

    if(cloud_env == 'azure'):
        return Azure()
    elif(cloud_env == 'gcp'):
        return Gcp()
    elif(cloud_env == 'aws'):
        return Aws()

    raise Exception(f"The CLOUD environment variable (value: {cloud_env}) is not recognized")

cloud_provider = get_cloud_provider()

cloud_provider.configure()
cloud_provider.terraform_apply()
cloud_provider.kubernetes_apply(".")

print('\033[92mSuccess :)')



