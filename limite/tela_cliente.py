class TelaCliente:
    def __init__(self, controlador_cliente):
        self.__controle = controlador_cliente

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
        print(" ---- Cadastro de Clientes ---- ")
        print("Escolha a opção")
        print("1: Inclui Cliente")
        print("2: Exclui Cliente")
        print("3: Lista Clientes")
        print("4: Altera dados do Cliente")
        print("0: Retorna")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def solicita_dados_cliente(self):
        print(" ---- Inclusão de Cliente ---- ")
        nome = input("Nome do cliente: ")
        data_nascimento = input("Data de nascimento: ")
        telefone = input("Telefone: ")
        instagram = input("Instagram: ")
        tipo_cliente = input("Tipo cliente: ")
        obs = input("Observações: ")
        return {"Nome": nome, "Data_nascimento": data_nascimento, "Telefone": telefone, "Instagram": instagram, "Tipo_cliente": tipo_cliente, "Obs": obs}

    def mostra_dados_cliente(self, nome: str):
        print("Cliente: ", nome)

    def encontra_cliente(self):
        print(" ---- Exclusão de cliente ---- ")
        nome = input("Nome do cliente que deseja excluir: ")
        return nome

    def excecao(self, mensagem):
        print("Teste", mensagem)