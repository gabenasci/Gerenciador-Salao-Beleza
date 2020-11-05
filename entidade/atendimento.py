import datetime
from entidade.servico import Servico
from entidade.cliente import Cliente
from entidade.funcionario import Funcionario


class Atendimento:

    def __init__(self, servico: Servico, cliente: Cliente, funcionario: Funcionario, data: datetime.date,
             hora: datetime.time):
        self.__servico = servico
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__data = data
        self.__hora = hora

        @property
        def servico(self):
            return self.__servico

        @servico.setter
        def servico(self, servico):
            self.__servico = servico

        @property
        def cliente(self):
            return self.__cliente

        @cliente.setter
        def cliente(self, cliente):
            self.__cliente = cliente

        @property
        def funcionario(self):
            return self.__funcionario

        @funcionario.setter
        def funcionario(self, funcionario):
            self.__funcionario = funcionario

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

        @property
        def hora(self):
            return self.__hora

        @hora.setter
        def hora(self, hora):
            self.__hora = horas