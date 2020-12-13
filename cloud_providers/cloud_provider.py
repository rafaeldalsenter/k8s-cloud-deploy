import abc

class CloudProvider():

    @abc.abstractclassmethod
    def configure(self):
        pass

    @abc.abstractclassmethod
    def terraform_apply(self):
        pass

    @abc.abstractclassmethod
    def kubernetes_apply(self, dir):
        pass