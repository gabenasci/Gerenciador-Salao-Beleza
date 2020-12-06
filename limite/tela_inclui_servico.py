import PySimpleGUI as sg


class TelaIncluiServico:
    def __init__(self, controlador_servico):
        self.__controlador = controlador_servico
        self.__window = None
        self.init_components(None, None)


    def init_components(self, nome, requisito):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Nome: ', size=(40, 1)), sg.InputText(nome, key='it_nome')],
                    [sg.Text('Requisito: ', size=(40, 1)), sg.InputText(requisito, key='it_requisito')],
                    [sg.Submit('Salvar'), sg.Cancel('Voltar')]
                ]

        self.__window = sg.Window('Cadastro de serviço', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()