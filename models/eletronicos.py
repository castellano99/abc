from models.abstract_eletronico import Eletronico

class iPhone16(Eletronico):
    def __init__(self):
        self.nome = "iPhone 16"

    def armazenamento(self):
        return "Armazenamento 256GB"

class S25(Eletronico):
    def __init__(self):
        self.nome = "S25"

    def armazenamento(self):
        return "Armazenamento 512GB"