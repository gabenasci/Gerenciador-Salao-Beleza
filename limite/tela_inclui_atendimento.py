import PySimpleGUI as sg


class TelaIncluiAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador = controlador_atendimento
        self.__window = None
        self.init_components(None, None, None, None, None, None, None, None, None)


    def init_components(self, id, servico, cliente, funcionario, data, hora, valor, pago, realizado):
        sg.ChangeLookAndFeel('Reddit')
        list = self.__controlador.get_servicos()
        
        

        layout = [
                    [sg.Text('Serviço: ', size=(40, 1)), sg.InputCombo(list, servico, size=(40, 1), key='it_servico')],
                    [sg.Text('Nome do Cliente: ', size=(40, 1)), sg.InputText(cliente, key='it_cliente')],
                    [sg.Text('Nome do Funcionario: ', size=(40, 1)), sg.InputText(funcionario, key='it_funcionario')],
                    [sg.Text('Data do atendimento (DIA/MES/ANO): ', size=(40, 1)), sg.InputText(data, key='it_data')],
                    [sg.Text('Hora do atendimento (HH:MM): ', size=(40, 1)), sg.InputText(hora, key='it_hora')],
                    [sg.Text('Valor: R$ ', size=(40, 1)), sg.InputText(valor, key='it_valor')],
                    [sg.Checkbox('Pago', size=(40, 1), key='pago'), sg.Checkbox('Realizado', size=(40,1), key='realizado')],
                    [sg.Submit('Salvar'), sg.Cancel('Voltar')]
                ]

        self.__window = sg.Window('Cadastro de atendimento', default_button_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def get_servicos(self):
        list = ['a', 'b', 'd']
        return list