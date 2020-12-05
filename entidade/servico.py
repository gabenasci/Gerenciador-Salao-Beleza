
class Servico:

    def __init__(self, nome: str, requisito: str):
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


