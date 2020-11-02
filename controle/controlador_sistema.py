from limite.tela_sistema import TelaSistema
from controle.controlador_cliente import ControladorCliente
from controle.controlador_servico import ControladorServico
from controle.controlador_funcionario import ControladorFuncionario


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_servico = ControladorServico(self)
        self.__controlador_funcionario = ControladorFuncionario(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def opcao_funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def opcao_clientes(self):
        self.__controlador_cliente.abre_tela()

    def opcao_servicos(self):
        self.__controlador_servico.abre_tela()

    def opcao_atendimentos(self):
        pass

    def opcao_encerra(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.opcao_funcionarios, 2: self.opcao_clientes,
                        3: self.opcao_servicos, 4: self.opcao_atendimentos,
                        0: self.opcao_encerra}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()

    def funcionarios(self):
        return self.__controlador_funcionario.funcionarios
