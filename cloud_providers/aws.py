from cloud_providers.cloud_provider import CloudProvider

class Aws(CloudProvider):

    def __init__(self):
        pass

    def configure(self):
        print('entrou no Aws')

    def terraform_apply(self):
        pass

    def kubernetes_apply(self, dir):
        pass