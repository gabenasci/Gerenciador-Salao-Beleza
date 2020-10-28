class TelaCliente:
    def __init__(self, controlador_cliente):
        self.__controle = controlador_cliente

    def tela_opcoes(self):
        print(" ---- Cadastro de Clientes ---- ")
        print("Escolha a opção")
        print("1: Inclui Cliente")
        print("2: Altera dados do Cliente")
        print("3: Lista Clientes")
        print("0: Retorna")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def solicita_dados_cliente(self):
        print(" ---- Inclusão de Cliente ---- ")
        nome = input("Nome do cliente: ")
        return {"nome": nome}

    def mostra_dados_cliente(self, nome: str):
        print("Cliente:", nome)