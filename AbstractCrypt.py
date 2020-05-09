from abc import ABC,abstractmethod

class Abstract(ABC):

    @abstractmethod
    def encrypt(self,text_path):
        pass

    @abstractmethod
    def decrypt(self,text_path):
        pass

    @abstractmethod
    def key_generator(self):
        pass


