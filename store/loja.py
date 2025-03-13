from factories.fabrica_moda import FabricaModa
from factories.fabrica_eletronico import FabricaEletronico

class Loja:
    def __init__(self):
        choice = input("Deseja comprar eletrônicos ou roupas?")
        if choice in ["eletrônicos", "eletronicos"]:
            self.venderEletronicos()
        elif choice == "roupas":
            self.venderRoupas()
        else:
            print("Não trabalhamos com esse tipo de produto")
    
    def venderEletronicos(self):
        fabrica = FabricaEletronico()
        produtos = fabrica.criarEletronico()
        print("Produtos disponíveis:")
        for i in produtos:
            print(f"{i.nome} - {i.armazenamento()}")

    def venderRoupas(self):
        fabrica = FabricaModa()
        produtos = fabrica.criarModa()
        print("Produtos disponíveis:")
        for i in produtos:
            print(f"{i.nome} - {i.preco()}" )