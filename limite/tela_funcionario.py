

class TelaFuncionario:
    def __init__(self, controlador_funcionario):
        self.__controlador = controlador_funcionario

    def tela_opcoes(self):
        print(" ---- Cadastro de Funcionarios ---- ")
        print("Escolha a opção")
        print("1: Inclui Funcionario")
        print("2: Altera dados do Funcionario")
        print("3: Lista Funcionarios")
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
        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                "data_contratacao": data_contratacao, "servico": servico}

    def mostra_dados_funcionario(self, nome: str):
        print("Nome:", nome)
