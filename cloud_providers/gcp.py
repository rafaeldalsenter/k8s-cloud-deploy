import os
from cloud_providers.cloud_provider import CloudProvider

class Gcp(CloudProvider):

    def __init__(self):
        self.__id_project = os.getenv('PROJECT_ID')
        self.__region = os.getenv('REGION')

        if(self.__id_project == None or self.__region == None):
            raise Exception("Set the PROJECT_ID and REGION environment variables")

    def configure(self):
        print('entrou no gcp')