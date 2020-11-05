class TelaServico:
    def __init__(self, controlador_servico):
        self.__controle = controlador_servico

    def tela_opcoes(self):
        print(" ---- Cadastro de Servicos ---- ")
        print("Escolha a opção")
        print("1: Inclui Serviço")
        print("2: Exclui Serviço")
        print("3: Lista Serviço")
        print("4: Altera dados do Serviço")
        print("5: Habilitar funcionário para um serviço")
        print("0: Retorna")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def solicita_dados_servico(self):
        print(" ---- Inclusão de Serviço ---- ")
        nome = input("Nome do serviço: ")
        ferramenta = input("Ferramenta necessária (Kit unha, Kit cabelo ou Kit pele): ")
        return {"Nome": nome, "Requisito": ferramenta}

    def mostra_dados_servico(self, nome: str, requisito: str):
        print("Serviço:", nome)
        print("Requisito:", requisito)

    def encontra_servico(self):
        print(" ---- Exclusão de cliente ---- ")
        nome = input("Nome do cliente que deseja excluir: ")
        return nome

    def encontra_funcionario(self):
        print(" ---- Habilita funcionário ---- ")
        funcionario = input("Nome do funcionário que deseja habilitar: ")
        servico = input("Para qual serviço deseja habilitar esse funcionário: ")
        return funcionario, servico

    def altera_dados_servico(self):
        print(" --- Alteração de servico ---")
        nome_servico = input("Nome do servico a ser alterado: ")
        print("Dados: nome, requisito")
        dado = input("Dado a ser alterado: ")
        valor = input("Insira o " + dado + ": ")
        return nome_servico, dado, valor
