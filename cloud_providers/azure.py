from cloud_providers.cloud_provider import CloudProvider

class Azure(CloudProvider):

    def configure(self):
        print('entrou no Azure')