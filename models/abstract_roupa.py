from abc import ABCMeta, abstractmethod

class Roupa(metaclass=ABCMeta):
    @abstractmethod
    def preco():
        pass