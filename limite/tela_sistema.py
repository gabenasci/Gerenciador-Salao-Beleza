import PySimpleGUI as sg


class TelaSistema():

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
                    [sg.Text('', justification='c', size=(15, 1))],
                    [sg.Text('Salão de Beleza',justification='c', size=(20, 1), font=("Helvetica", 25))],
                    [sg.Text('Escolha a opção: ')],
                    #[sg.InputText('Texto de resposta', key='it_nome')],
                    [sg.Button('Funcionario', size=(15, 2),font=('Helvetica', 20))],
                    [sg.Button('Cliente', size=(15, 2),font=('Helvetica', 20))],
                    [sg.Button('Servico', size=(15, 2),font=('Helvetica', 20))],
                    [sg.Button('Atendimento', size=(15, 2),font=('Helvetica', 20))],
                    [sg.Cancel('Sair', font=('Helvetica', 20),size=(15,2),button_color=('white','red'))]
                ]
        self.__window = sg.Window('Sistema Salão de Beleza', default_button_element_size=(40, 1), size=(400, 550), element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)