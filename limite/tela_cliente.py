import datetime
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
import PySimpleGUI as sg

class TelaCliente:
    def __init__(self, controlador_cliente):
        self.__controle = controlador_cliente
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = []
        headings = ['NOME', 'NASCIMENTO', 'TELEFONE', 'INSTAGRAM', 'TIPO', 'OBSERVAÇÃO']
        header = [[sg.Text('  ', size=(3, 0))] + [sg.Text(h, size=(15, 0)) for h in headings]]

        for cliente in self.__controle.clientes:
            layout += [[sg.Checkbox('', key=cliente.nome), sg.Text(cliente.nome, size=(15,1)), sg.Text(cliente.data_nascimento, size=(15,1)), sg.Text(cliente.telefone, size=(15,1)),
                        sg.Text(cliente.instagram, size=(15,1)), sg.Text(cliente.tipo_cliente, size=(15,1)), sg.Text(cliente.obs, size=(15,1))]]
        layout = header + layout + [[sg.Button('Incluir'), sg.Button('Excluir'), sg.Button('Alterar'), sg.Cancel('Voltar')]]
        self.__window = sg.Window('CLIENTES', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
