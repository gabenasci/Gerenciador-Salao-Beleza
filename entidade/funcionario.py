from entidade.pessoa import Pessoa
from entidade.servico import Servico
import datetime


class Funcionario(Pessoa):

    def __init__(self, nome: str, data_nascimento: datetime.date, telefone: int, data_contratacao: datetime.date):
        super().__init__(nome, data_nascimento, telefone)
        if isinstance(data_contratacao, datetime.date):
            self.__data_contratacao = data_contratacao
        self.__servicos = []

    @property
    def data_contratacao(self):
        return self.__data_contratacao

    @data_contratacao.setter
    def data_contratacao(self, data_contratacao: datetime.date):
        if isinstance(data_contratacao, datetime.date):
            self.__data_contratacao = data_contratacao

    @property
    def servicos(self):
        return self.__servicos

    @servicos.setter
    def servicos(self, servicos):
        self.__servicos = servicos

    def add_servico(self, servico, Servico):
        if (servico is not None) and (isinstance(servico, Servico)):
            if servico not in self.__servicos:
                self.__servicos.append(servico)
                #for a in self.__funcionarios:
                    #print(a.nome)
            if self not in servico.funcionarios:
                servico.funcionarios.append(self)
                #for i in funcionario.servicos:
                    #print(i.nome)
