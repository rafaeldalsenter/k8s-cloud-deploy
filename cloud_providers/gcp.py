from cloud_providers.cloud_provider import CloudProvider

class Gcp(CloudProvider):

    def configure(self):
        print('entrou no gcp')