import datetime

class TelaFuncionario:
    def __init__(self, controlador_funcionario):
        self.__controlador = controlador_funcionario

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
        print(" ---- Cadastro de Funcionarios ---- ")
        print("Escolha a opção")
        print("1: Inclui Funcionario")
        print("2: Exclui Funcionario")
        print("3: Lista Funcionarios")
        print("4: Altera dados do Funcionario")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        return opcao

    def solicita_dados_funcionario(self):
        print(" ---- Inclusão de Funcionario ---- ")
        nome = input("Nome do funcionário: ")
        data = input("Data de nascimento do funcionário (DIA/MES/ANO): ")
        dia, mes, ano = map(int, data.split('/'))
        data_nascimento = datetime.date(ano, mes, dia)
        telefone = int(input("Telefone do funcionário: "))
        data2 = input("Data de contratação do funcionário (DIA/MES/ANO): ")
        dia, mes, ano = map(int, data2.split('/'))
        data_contratacao = datetime.date(ano, mes, dia)
        dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                             "data_contratacao": data_contratacao}
        return dados_funcionario

    def mostra_dados_funcionario(self, nome: str, data_nascimento, data_contratacao):
        print("Nome: ", nome)
        print("Data Nascimento: ", data_nascimento)
        print("Data contratação: ", data_contratacao)

    def encontra_funcionario(self):
        print(" ---- Exclusão de funcionario ---- ")
        nome = input("Nome do funcionario que deseja excluir: ")
        return nome

    def altera_dados_funcionario(self):
        print(" --- Alteração de funcionario ---")
        nome_funcionario = input("Nome do funcionario a ser alterado: ")
        print("Dados: nome, data_nascimento, telefone, data_contratacao, servico")
        dado = input("Dado a ser alterado ")
        if dado == "data_nascimento" or "data_contratacao":
            data = input("Insira o " + dado +" (DIA/MÊS/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            valor = datetime.date(ano, mes, dia)
        else:
            valor = input("Insira o " + dado + ": ")
        return nome_funcionario, dado, valor


