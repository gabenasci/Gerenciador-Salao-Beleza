

class TelaFuncionario:
    def __init__(self, controlador_funcionario):
        self.__controlador = controlador_funcionario

    def tela_opcoes(self):
        print(" ---- Cadastro de Funcionarios ---- ")
        print("Escolha a opção")
        print("1: Inclui Funcionario")
        print("2: Exclui Funcionario")
        print("3: Lista Funcionarios")
        print("4: Altera dados do Funcionario")
        print("0: Retorna")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def solicita_dados_funcionario(self):
        print(" ---- Inclusão de Funcionario ---- ")
        nome = input("Nome do funcionário: ")
        data_nascimento = input("Data de nascimento do funcionário: ")
        telefone = int(input("Telefone do funcionário: "))
        data_contratacao = input("Data de contratação do funcionário: ")
        servico = input("Servico: ")
        dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                "data_contratacao": data_contratacao, "servico": servico}
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
        print("Dados: nome, data_nascimento, telfone, data_contratacao, servico")
        dado = input("Qual o dado a ser alterado? ")
        valor = input("Insira o novo " + dado +": ")
        return nome_funcionario, dado, valor


