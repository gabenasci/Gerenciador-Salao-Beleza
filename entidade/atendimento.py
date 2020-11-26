import datetime
from entidade.servico import Servico
from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.pagamento import Pagamento


class Atendimento:

    def __init__(self, servico: Servico, cliente: Cliente, funcionario: Funcionario, data: datetime.date,
                 hora: datetime.time, valor: float, pago: bool, realizado: bool):
        if isinstance(servico, Servico):
            self.__servico = servico
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario
        if isinstance(data, datetime.date):
            self.__data = data
        if isinstance(hora, datetime.time):
            self.__hora = hora
        if isinstance(valor, float) and isinstance(pago, bool):
            self.__pagamento = Pagamento(valor, pago)
        self.__id = 0
        if isinstance(realizado, bool):
            self.__realizado = realizado

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
        self.__hora = hora

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def valor(self):
        return self.__pagamento.valor

    @property
    def pago(self):
        return self.__pagamento.pago

    @property
    def realizado(self):
        return self.__realizado
