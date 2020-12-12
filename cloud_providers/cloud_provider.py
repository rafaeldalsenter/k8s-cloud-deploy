import abc

class CloudProvider():

    @abc.abstractclassmethod
    def configure(self):
        pass