import datetime
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
import PySimpleGUI as sg


class TelaFuncionario:
    def __init__(self, controlador_funcionario):
        self.__controlador = controlador_funcionario
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        lista = []

        headings = ['NOME', 'NASCIMENTO', 'TELEFONE', 'CONTRATAÇÃO']
        header = [[sg.Text('  ',size=(3,0))] + [sg.Text(h, size=(15, 0)) for h in headings]]

        for funcionario in self.__controlador.funcionarios:
            lista += [[sg.Checkbox('', key=funcionario.nome), sg.Text(funcionario.nome, size=(15,1)), sg.Text(funcionario.data_nascimento,size=(15,1)),
                        sg.Text(funcionario.telefone,size=(15,1)), sg.Text(funcionario.data_contratacao,size=(15,1))]]

        layout = header + lista + [[sg.Button('Incluir'), sg.Button('Excluir'), sg.Button('Alterar'), sg.Cancel('Voltar')]]

        self.__window = sg.Window('FUNCIONÁRIO', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def excecao(self, mensagem):
        print(mensagem)
