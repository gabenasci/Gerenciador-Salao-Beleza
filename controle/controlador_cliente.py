from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente

class ControladorCliente:

    def __init__(self, controlador_sistema):
        self.__clientes = []

        self.__controlador = controlador_sistema
        self.__tela_cliente = TelaCliente(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_cliente, 3: self.exclui_cliente, 4: self.lista_clientes, 5: self.altera_cliente}

        while self.__continua_exibindo_tela:
            opcao = self.__tela_cliente.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.solicita_dados_cliente()
        novo_cliente = Cliente(dados_cliente["Nome"])
        self.__clientes.append(novo_cliente)

    def exclui_cliente(self):
        pass

    def lista_clientes(self):
        pass

    def altera_cliente(self):
        pass

    def retorna(self):
        self.__continua_exibindo_tela = False