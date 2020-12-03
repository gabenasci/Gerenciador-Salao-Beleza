import datetime
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
import PySimpleGUI as sg

class TelaFiltraAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador = controlador_atendimento
        self.__window = None
        self.init_components([])

    def init_components(self, atendimentos):
        sg.ChangeLookAndFeel('Reddit')

        lista = []

        headings = ['ID', 'SERVICO', 'CLIENTE', 'FUNCIONARIO', 'DATA', 'HORA', 'VALOR', 'PAGO', 'REALIZADO']
        header = [[sg.Text('  ',size=(3,0))] + [sg.Text(h, size=(15, 0)) for h in headings]]

        for atendimento in atendimentos:
            lista += [[sg.Checkbox('', key=atendimento.id), sg.Text(atendimento.id, size=(15,1)), sg.Text(atendimento.servico.nome, size=(15,1)), sg.Text(atendimento.cliente.nome, size=(15,1)), sg.Text(atendimento.funcionario.nome,size=(15,1)),
                       sg.Text(atendimento.data,size=(15,1)), sg.Text(atendimento.hora,size=(15,1)), sg.Text(atendimento.valor,size=(15,1)),
                       sg.Text(atendimento.pago,size=(15,1)), sg.Text(atendimento.realizado,size=(15,1))]]

        layout = header + lista + [[sg.Cancel('Voltar')]]

        self.__window = sg.Window('Cadastro de atendimento', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
