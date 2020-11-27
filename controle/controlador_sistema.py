from limite.tela_sistema import TelaSistema
from controle.controlador_cliente import ControladorCliente
from controle.controlador_servico import ControladorServico
from controle.controlador_funcionario import ControladorFuncionario
from controle.controlador_atendimento import ControladorAtendimento
import PySimpleGUI as sg

class ControladorSistema():
    __instance = None

    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_servico = ControladorServico(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_atendimento = ControladorAtendimento(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    def inicializa_sistema(self):
        self.abre_tela()
        '''
        while True:
            self.abre_tela()
            if event == 'Gravar':
                print('Gravar funcionando')
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            print(event)
        '''

    def abre_tela(self):
        lista_opcoes = {'Funcionario': self.opcao_funcionarios, 'Cliente': self.opcao_clientes,
                        'Servico': self.opcao_servicos, 'Atendimento': self.opcao_atendimentos,
                        'Cancelar': self.opcao_encerra}

        while True:
            button, values = self.__tela_sistema.open()
            if button == sg.WIN_CLOSED:
                exit(0)
            funcao_escolhida = lista_opcoes[button]

            funcao_escolhida()

    def opcao_funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def opcao_clientes(self):
        self.__controlador_cliente.abre_tela()

    def opcao_servicos(self):
        self.__controlador_servico.abre_tela()

    def opcao_atendimentos(self):
        self.__controlador_atendimento.abre_tela()

    def opcao_encerra(self):
        exit(0)

    @property
    def controlador_servico(self):
        return self.__controlador_servico

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento
