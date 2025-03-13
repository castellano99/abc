from models.abstract_roupa import Roupa

class JeansJovem16anos(Roupa):
    def __init__(self):
        self.nome = "Calça p/ uma jovem de 16 anos"

    def preco(self):
        return "Custa mais de 300 reais"

class Camisa(Roupa):
    def __init__(self):
        self.nome = "Camisa"

    def preco(self):
        return "100 reais"