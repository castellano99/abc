from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def criarModa(self):
        pass

    @abstractmethod
    def criarEletronico(self):
        pass