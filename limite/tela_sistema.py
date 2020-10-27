

class TelaSistema():
    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema

    def tela_opcoes(self):
        print("===== Tela de Opções =====")
        print("Escolha a opção:")
        print("1: Funcionario")
        print("2: Cliente")
        print("3: Serviços")
        print("4: Atendimentos")
        print("0: Encerrar o Sistema")

        opcao = int(input("Escolha a opção: "))
        return opcao