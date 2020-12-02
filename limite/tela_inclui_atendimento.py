import PySimpleGUI as sg


class TelaIncluiAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador = controlador_atendimento
        self.__window = None
        self.init_components(None, None, None, None, None, None, None, None, None)


    def init_components(self, id, servico, cliente, funcionario, data, hora, valor, pago, realizado):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    #[sg.Text('Cadastro de Funcionário', size=(30, 1), font=("Helvetica", 25))],
                    [sg.Text('Serviço a ser marcado: ', size=(40, 1)), sg.InputText(servico, key='it_servico')],
                    [sg.Text('Nome do Cliente: ', size=(40, 1)), sg.InputText(cliente, key='it_cliente')],
                    [sg.Text('Nome do Funcionario: ', size=(40, 1)), sg.InputText(funcionario, key='it_funcionario')],
                    [sg.Text('Data do atendimento (DIA/MES/ANO): ', size=(40, 1)), sg.InputText(data, key='it_data')],
                    [sg.Text('Hora do atendimento (HH:MM): ', size=(40, 1)), sg.InputText(hora, key='it_hora')],
                    [sg.Text('Valor: R$ ', size=(40, 1)), sg.InputText(valor, key='it_valor')],
                    [sg.Checkbox('Pago agora', size=(40, 1), key='pago'), sg.Checkbox('Realizado', size=(40,1), key='realizado')],
                    #[sg.Output('')]
                    [sg.Submit('Salvar'), sg.Cancel('Voltar')]
                ]

        self.__window = sg.Window('Cadastro de atendimento', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()