from abc import ABC,abstractmethod

class Abstract(ABC):

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass

    @abstractmethod
    def key_generator(self):
        pass


