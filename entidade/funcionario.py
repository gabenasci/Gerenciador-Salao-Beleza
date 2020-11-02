from entidade.pessoa import Pessoa
from entidade.servico import Servico


class Funcionario(Pessoa):

    def __init__(self, nome: str, data_nascimento: str, telefone: int, data_contratacao: str, servico: Servico):
        super().__init__(nome, data_nascimento, telefone)
        if isinstance(data_contratacao, str):
            self.__data_contratacao = data_contratacao
        #if isinstance(servico, Servico):
            self.__servico = servico

    @property
    def data_contratacao(self):
        return self.__data_contratacao

    @data_contratacao.setter
    def data_contratacao(self, data_contratacao):
        self.__data_contratacao = data_contratacao

    @property
    def servico(self):
        return self.__servico

    @servico.setter
    def servico(self, servico):
        self.__servico = servico