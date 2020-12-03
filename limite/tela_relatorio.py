import PySimpleGUI as sg

class TelaRelatorio:
    def __init__(self, controlador_atendimento):
        self.__controlador = controlador_atendimento
        self.__window = None
        self.__lista = []
        self.init_components({})

    def init_components(self, contador_servicos):
        sg.ChangeLookAndFeel('Reddit')
        lista = [[sg.Text('Número de vezes que um serviço foi agendado no mês escolhido', justification = 'center')]]
        for chave, valor in contador_servicos.items():
            lista += [[sg.Text(str(chave) + ': ' + str(valor) + 'x')]]

        layout = lista

        self.__window = sg.Window('RELATÓRIO MENSAL', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
