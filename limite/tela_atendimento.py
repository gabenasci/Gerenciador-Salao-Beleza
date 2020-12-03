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


    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico inteiro válido")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def tela_opcoes(self):
        print(" ---- ATENDIMENTOS ---- ")
        print("Escolha a opção")
        print("1: Marcar Atendimento")
        print("2: Excluir Atendimento")
        print("3: Alterar Atendimento")
        print("4: Listar Atendimentos por Cliente")
        print("5: Listar Atendimentos por Dia")
        print("6: Relatório do mês - número de atendimentos por serviço")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 6, 0])
        return opcao

    def solicita_dados_atendimento(self):
        print(" ---- Marcar Atendimento ---- ")
        try:
            servico = input("Serviço a ser marcado: ")
            if servico not in self.__controle.servicos():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Serviço não existe!")
            self.__controle.abre_tela()
        try:
            cliente = input("Nome do cliente: ")
            if cliente not in self.__controle.clientes():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Cliente não existe!")
            self.__controle.abre_tela()
        try:
            funcionario = input("Nome do funcionário: ")
            if funcionario not in self.__controle.funcionarios():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Funcionário não existe!")
            self.__controle.abre_tela()
        try:
            data = input("Data do atendimento (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            data_atendimento = datetime.date(ano, mes, dia)
            if data_atendimento < datetime.date.today():
                raise ValueError
        except ValueError:
            print ("Data inválida!")
            self.__controle.abre_tela()
        try:
            hora = input("Hora do atendimento (HH:MM): ")
            h, m = map(int, hora.split(':'))
            hora_atendimento = datetime.time(h, m)
        except ValueError:
            print("Horário inválido!")
            self.__controle.abre_tela()
        valor = input("Valor do atendimento: R$")
        try:
            valor = float(valor)
        except ValueError:
            print("Valor float inválido")
            self.__controle.abre_tela()
        pago = input("Pago agora (True/False):")
        try:
            if pago == "True":
                pago = True
            elif pago == "False":
                pago = False
        except ValueError:
            print("Valor booleano inválido")
            self.__controle.abre_tela()
        realizado = False
        dados_atendimento = {"servico": servico, "cliente": cliente, "funcionario": funcionario,
                                 "data": data_atendimento, "hora": hora_atendimento, "valor": valor, "pago": pago,
                             "realizado": realizado}
        return dados_atendimento

    def encontra_atendimento(self):
        print(" ---- Exclusão de Atendimento ---- ")
        id = int(input("Insira o ID do atendimento para excluir: "))
        return id

    def altera_dados_atendimento(self):
        print(" ---- Alteração de Atendimento ----")
        id = input("Insira o ID do atendimento: ")
        try:
            id = int(id)
        except ValueError:
            print("Tipo de valor inválido! Insira um número inteiro.")
            self.__controle.abre_tela()
        print("Dados: servico, cliente, funcionario, data, hora, valor, pago, realizado")
        try:
            dado = input("Dado a ser alterado: ")
            if dado == "data":
                try:
                    data = input("Insira a " + dado +" (DIA/MÊS/ANO): ")
                    dia, mes, ano = map(int, data.split('/'))
                    valor = datetime.date(ano, mes, dia)
                    if valor < datetime.date.today():
                        raise ValueError
                except ValueError:
                    print("Data inválida!")
                    self.__controle.abre_tela()
            elif dado == "hora":
                try:
                    hora = input("Insira a "+ dado +"(HH:MM): ")
                    h, m = map(int, hora.split(':'))
                    valor = datetime.time(h, m)
                except ValueError:
                    print("Horário inválido!")
                    self.__controle.abre_tela()
            elif dado == "pago":
                valor = input("Insira o "+dado+"(True/False): ")
                try:
                    valor = bool(valor)
                except ValueError:
                    print("Valor booleano inválido!")
                    self.__controle.abre_tela()
            elif dado == "valor":
                valor = input("Insira o "+dado+": ")
                try:
                    valor = float(valor)
                except ValueError:
                    print("Valor float inválido!")
                    self.__controle.abre_tela()
            elif dado == "cliente" or dado == "servico" or dado == "funcionario":
                valor = input("Insira o " + dado + ": ")
            elif dado == "realizado":
                valor = input("Atendimento foi realizado? (True/False): ")
                if valor == "True":
                    valor = True
                elif valor == "False":
                    valor = False
            else:
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados válidos: servico, cliente, funcionario, data, hora, valor, pago, realizado")
            self.__controle.abre_tela()
        return id, dado, valor

    def atendimento_cliente(self):
        print(" ---- Atendimentos por Cliente ---- ")
        cliente = input("Insira o nome do cliente: ")
        return cliente

    def atendimento_dia(self):
        print(" ---- Atendimentos por Dia ---- ")
        try:
            data = input("Insira a data (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            data_atendimento = datetime.date(ano, mes, dia)
        except ValueError:
            print("Data inválida!")
            self.__controle.abre_tela()
        return data_atendimento

    def mostra_dados_atendimento(self, id: int, servico, cliente, funcionario, data, hora, valor, pago, realizado):
        print("ID: ", id)
        print("Servico: ", servico.nome)
        print("Cliente: ", cliente.nome)
        print("Funcionario: ", funcionario.nome)
        print("Data e hora: "+str(data)+ ", ", str(hora))
        print("Valor: R$", str(valor))
        print("Pago: ", str(pago))
        print("Realizado: ", str(realizado))
        print("--------------------")

    def relatorio_mes(self):
        print(" ---- Relatório do Mês ---- ")
        mes = input("Insira o mês (1-12): ")
        try:
            mes = int(mes)
            if mes > 12 or mes < 1:
                raise ValueError
        except ValueError:
            print("Mês inválido!")
            self.__controle.abre_tela()
        return mes

    def mostra_relatorio(self):
        pass

    def excecao(self, mensagem):
        print(mensagem)