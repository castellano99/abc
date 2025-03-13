from factories.abstract_factory import AbstractFactory
from models.roupas import JeansJovem16anos, Camisa


class FabricaModa(AbstractFactory):
    def criarModa(self):
        return [JeansJovem16anos(), Camisa()]
    
    def criarEletronico(self):
        return None