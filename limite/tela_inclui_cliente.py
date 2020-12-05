import PySimpleGUI as sg
from entidade.cliente import Cliente


class TelaIncluiCliente:
    def __init__(self, controlador_cliente):
        self.__controlador = controlador_cliente
        self.__window = None
        self.init_components(None, None, None, None, None, None)


    def init_components(self, nome, data_n, telefone, instagram, tipo_cliente, obs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Nome: ', size=(40, 1)), sg.InputText(nome, key='it_nome')],
                    [sg.Text('Data de Nascimento (DIA/MES/ANO): ', size=(40, 1)), sg.InputText(data_n, key='it_data_nascimento')],
                    [sg.Text('Telefone: ', size=(40, 1)), sg.InputText(telefone, key='it_telefone')],
                    [sg.Text('Instagram: ', size=(40, 1)), sg.InputText(instagram, key='it_instagram')],
                    [sg.Text('Tipo cliente: ', size=(40, 1)), sg.Radio(Cliente.TIPO_CLIENTE[0], "RD_TIPO_CLIENTE", size=(10, 1), key=Cliente.TIPO_CLIENTE[0]), sg.Radio(Cliente.TIPO_CLIENTE[1], "RD_TIPO_CLIENTE", key=Cliente.TIPO_CLIENTE[1]), sg.Radio(Cliente.TIPO_CLIENTE[2], "RD_TIPO_CLIENTE", key=Cliente.TIPO_CLIENTE[2])],
                    [sg.Text('Observações: ', size=(40, 1)), sg.InputText(obs, key='it_obs')],
                    [sg.Submit('Salvar'), sg.Cancel('Voltar')]
                ]

        self.__window = sg.Window('Cadastro de cliente', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
