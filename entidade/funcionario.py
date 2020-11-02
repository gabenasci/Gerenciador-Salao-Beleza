from entidade.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome: str, data_nascimento: str, telefone: int, data_contratacao: str):
        super().__init__(nome, data_nascimento, telefone)
        if isinstance(data_contratacao, str):
            self.__data_contratacao = data_contratacao
        self.__servicos = []

    @property
    def data_contratacao(self):
        return self.__data_contratacao

    @data_contratacao.setter
    def data_contratacao(self, data_contratacao):
        self.__data_contratacao = data_contratacao

    @property
    def servicos(self):
        return self.__servicos

    @servicos.setter
    def servicos(self, servicos):
        self.__servicos = servicos