from factories.abstract_factory import AbstractFactory
from models.eletronicos import iPhone16 , S25

class FabricaEletronico(AbstractFactory):
    def criarModa(self):
        return None

    def criarEletronico(self):
        return [iPhone16(), S25()]