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

        layout = []

        for funcionario in self.__controlador.funcionarios:
            layout += [[sg.Checkbox('', key=funcionario.nome), sg.Text(funcionario.nome), sg.Text(funcionario.data_nascimento), sg.Text(funcionario.telefone), sg.Text(funcionario.data_contratacao)]]

        layout += [[sg.Button('Incluir'), sg.Button('Excluir'), sg.Button('Alterar'), sg.Cancel('Voltar')]]

        self.__window = sg.Window('Cadastro de funcionário', default_button_element_size=(40, 1)).Layout(layout)

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
        print(" ---- FUNCIONÁRIOS ---- ")
        print("Escolha a opção")
        print("1: Inclui Funcionário")
        print("2: Exclui Funcionário")
        print("3: Lista Funcionários")
        print("4: Altera dados do Funcionário")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        return opcao

    def solicita_dados_funcionario(self):
        print(" ---- Inclusão de Funcionário ---- ")
        nome = input("Nome do funcionário: ")
        try:
            data = input("Data de nascimento do funcionário (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            data_nascimento = datetime.date(ano, mes, dia)
        except ValueError:
            print("Data inválida!")
            self.__controlador.abre_tela()
        telefone = input("Telefone do funcionário: ")
        try:
            telefone = int(telefone)
        except ValueError:
            print("Valor inteiro inválido!")
            self.__controlador.abre_tela()
        try:
            data2 = input("Data de contratação do funcionário (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data2.split('/'))
            data_contratacao = datetime.date(ano, mes, dia)
        except ValueError:
            print("Data inválida!")
            self.__controlador.abre_tela()
        dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                             "data_contratacao": data_contratacao}
        return dados_funcionario

    def mostra_dados_funcionario(self, nome: str, data_nascimento, data_contratacao):
        print("Nome: ", nome)
        print("Data Nascimento: ", str(data_nascimento))
        print("Data contratação: ", str(data_contratacao))
        print("--------------------")

    def encontra_funcionario(self):
        print(" ---- Exclusão de Funcionário ---- ")
        nome = input("Nome do funcionário que deseja excluir: ")
        return nome


    def altera_dados_funcionario(self):
        print(" ---- Alteração de funcionário ----")
        try:
            nome_funcionario = input("Nome do funcionário a ser alterado: ")
            if nome_funcionario not in self.__controlador.funcionarios_nome():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Funcionario não existe")
            self.__controlador.abre_tela()
        print("Dados: nome, data_nascimento, telefone, data_contratacao, servico")
        try:
            dado = input("Dado a ser alterado: ")
            if dado == "data_nascimento" or dado == "data_contratacao":
                try:
                    data = input("Insira o " + dado +" (DIA/MÊS/ANO): ")
                    dia, mes, ano = map(int, data.split('/'))
                    valor = datetime.date(ano, mes, dia)
                except ValueError:
                    print("Data inválida!")
                    self.__controlador.abre_tela()
            elif dado == "nome":
                valor = input("Insira o " + dado + ": ")
            elif dado == "telefone":
                valor = input("Insira o "+dado+": ")
                try:
                    valor = int(valor)
                except ValueError:
                    print("Valor inteiro inválido!")
                    self.__controlador.abre_tela()
            else:
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados válidos: nome, data_nascimento, telefone, data_contratacao, servico")
            self.__controlador.abre_tela()
        return nome_funcionario, dado, valor

    def excecao(self, mensagem):
        print(mensagem)
