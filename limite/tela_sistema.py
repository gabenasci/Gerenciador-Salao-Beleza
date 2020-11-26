import PySimpleGUI as sg


class TelaSistema():

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
                    [sg.Text('Sistema Salão de Beleza', size=(30, 1), font=("Helvetica", 25))],
                    [sg.Text('Escolha a opção: ')],
                    #[sg.InputText('Texto de resposta', key='it_nome')],
                    [sg.Button('Funcionario'), sg.Button('Cliente'),  sg.Button('Servico')],
                    [sg.Button('Atendimento'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('Titulo da tela', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)