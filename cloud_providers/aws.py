from cloud_providers.cloud_provider import CloudProvider

class Aws(CloudProvider):

    def configure(self):
        print('entrou no Aws')