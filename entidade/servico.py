from entidade.ferramenta import Ferramenta


class Servico:
    def __init__(self, nome: str, requisito: Ferramenta):
        self.__nome = nome
        self.__requisito = requisito

    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def requisito(self):
        return self.__requisito

    @requisito.setter
    def requisito(self, requisito):
        self.__nome = requisito

    kit_unha = Ferramenta("Kit unha")
    kit_cabelo = Ferramenta("Kit cabelo")
    kit_pele = Ferramenta("Kit pele")
