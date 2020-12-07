import datetime
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
import PySimpleGUI as sg

class TelaAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador = controlador_atendimento
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        lista = []

        headings = ['ID', 'SERVICO', 'CLIENTE', 'FUNCIONARIO', 'DATA', 'HORA', 'VALOR', 'PAGO', 'REALIZADO']
        header = [[sg.Text('  ',size=(3,0))] + [sg.Text(h, size=(15, 0)) for h in headings]]

        for atendimento in self.__controlador.atendimentos:
            lista += [[sg.Checkbox('', key=atendimento.id), sg.Text(atendimento.id, size=(15,1)), sg.Text(atendimento.servico.nome, size=(15,1)), sg.Text(atendimento.cliente.nome, size=(15,1)), sg.Text(atendimento.funcionario.nome,size=(15,1)),
                       sg.Text(atendimento.data,size=(15,1)), sg.Text(atendimento.hora,size=(15,1)), sg.Text(atendimento.valor,size=(15,1)),
                       sg.Text(atendimento.pago,size=(15,1)), sg.Text(atendimento.realizado,size=(15,1))]]
        botoes = [[sg.Text('Escolha o mês:',size=(15,0)), sg.Spin(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), initial_value='1', key='mes'), sg.Text('  ',size=(3,0)), sg.Button('Gerar relatório mensal')],
                    [sg.InputText('', key=('cliente')), sg.Button('Filtrar por cliente'), sg.InputText('',key=('data')), sg.Button('Filtrar por data')]]

        layout = header + lista + botoes + [[sg.Button('Incluir'), sg.Button('Excluir'), sg.Button('Alterar'), sg.Cancel('Voltar')]]

        self.__window = sg.Window('ATENDIMENTO', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def excecao(self, mensagem):
        print(mensagem)