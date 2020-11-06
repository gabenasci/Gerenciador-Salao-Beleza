

class TelaSistema():
    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema

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
        print("===== Tela de Opções =====")
        print("Escolha a opção:")
        print("1: Funcionario")
        print("2: Cliente")
        print("3: Serviços")
        print("4: Atendimentos")
        print("0: Encerrar o Sistema")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        return opcao