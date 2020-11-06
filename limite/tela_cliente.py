import datetime
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao

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
        print(" ---- CLIENTES ---- ")
        print("Escolha a opção")
        print("1: Inclui Cliente")
        print("2: Exclui Cliente")
        print("3: Lista Clientes")
        print("4: Altera dados do Cliente")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        return opcao

    def solicita_dados_cliente(self):
        print(" ---- Inclusão de Cliente ---- ")
        nome = input("Nome do cliente: ")
        try:
            data = input("Data de nascimento (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            data_nascimento = datetime.date(ano, mes, dia)
        except ValueError:
            print("Valor incorreto, insira uma data no formato DD/MM/AAAA")
            self.__controle.abre_tela()
        telefone = input("Telefone: ")
        try:
            telefone = int(telefone)
        except ValueError:
            print("Valor incorreto. Digite um número inteiro.")
            self.__controle.abre_tela()
        instagram = input("Instagram: ")
        tipo_cliente = input("Tipo cliente: ")
        obs = input("Observações: ")

        return {"Nome": nome, "Data_nascimento": data_nascimento, "Telefone": telefone, "Instagram": instagram,
                "Tipo_cliente": tipo_cliente, "Obs": obs}

    def mostra_dados_cliente(self, nome: str, telefone: int, data_nascimento:datetime, instagram: str, tipo_cliente: str, obs: str):
        print("Cliente: ", nome)
        print("Telefone: ", telefone)
        print("Data de nasicmento: ", data_nascimento)
        print("Instagram: ", instagram)
        print("Tipo cliente: ", tipo_cliente)
        print("Observação: ", obs)
        print("--------------------")

    def encontra_cliente(self):
        print(" ---- Exclusão de Cliente ---- ")
        nome = input("Nome do cliente que deseja excluir: ")
        return nome

    def altera_dados_cliente(self):
        print(" ---- Alteração de Cliente ----")
        try:
            nome_cliente = input("Nome do cliente a ser alterado: ")
            if nome_cliente not in self.__controle.clientes_nome():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Cliente não existe!")
            self.__controle.abre_tela()
        print("Dados: nome, data_nascimento, telefone, instagram, tipo_cliente, obs")
        try:
            dado = input("Dado a ser alterado: ")
            if dado == "data_nascimento":
                try:
                    data = input("Insira a " + dado +" (DIA/MÊS/ANO): ")
                    dia, mes, ano = map(int, data.split('/'))
                    valor = datetime.date(ano, mes, dia)
                except ValueError:
                    print("Data inválida!")
                    self.__controle.altera_cliente()
            elif dado == "telefone":
                valor = input("Insira o "+dado+":")
                try:
                    valor = int(valor)
                except ValueError:
                    print("Telefone precisa ser um número inteiro!")
                    self.__controle.altera_cliente()
            elif dado == "nome" or dado == "instagram" or dado == "tipo_cliente" or dado == "obs":
                valor = input("Insira o " + dado + ": ")
            else:
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados válidos: nome, data_nascimento, telefone, instagram, tipo_cliente, obs")
            self.__controle.abre_tela()
        return nome_cliente, dado, valor
    '''

    def altera_dados_cliente(self):
        print(" ---- Alteração de Cliente ----")
        nome_cliente = input("Nome do cliente a ser alterado: ")
        print("Dados: nome, data_nascimento, telefone, instagram, tipo_cliente, obs")
        try:
            dado = input("Dado a ser alterado: ")
            if dado == "data_nascimento":
                try:
                    data = input("Insira a " + dado +" (DIA/MÊS/ANO): ")
                    dia, mes, ano = map(int, data.split('/'))
                    valor = datetime.date(ano, mes, dia)
                except ValueError:
                    print("Data inválida!")
                    self.__controle.altera_cliente()
            elif dado == "telefone":
                valor = input("Insira o "+dado+":")
                try:
                    valor = int(valor)
                except ValueError:
                    print("Telefone precisa ser um número inteiro!")
                    self.__controle.altera_cliente()
            elif dado == "nome" or dado == "instagram" or dado == "tipo_cliente" or dado == "obs":
                valor = input("Insira o " + dado + ": ")
            else:
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados válidos: nome, data_nascimento, telefone, instagram, tipo_cliente, obs")
            self.__controle.abre_tela()
        return nome_cliente, dado, valor
    
    '''

    def excecao(self, mensagem):
        print(mensagem)