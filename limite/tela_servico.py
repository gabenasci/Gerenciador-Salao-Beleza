from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao

class TelaServico:
    def __init__(self, controlador_servico):
        self.__controle = controlador_servico

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
        print(" ---- SERVIÇOS ---- ")
        print("Escolha a opção")
        print("1: Inclui Serviço")
        print("2: Exclui Serviço")
        print("3: Lista Serviço")
        print("4: Altera dados do Serviço")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        return opcao

    def solicita_dados_servico(self):
        print(" ---- Inclusão de Serviço ---- ")
        nome = input("Nome do serviço: ")
        ferramenta = input("Ferramenta necessária (Kit unha, Kit cabelo ou Kit pele): ")
        try:
            if ferramenta == "kit unha" or ferramenta == "kit cabelo" or ferramenta == "kit pele":
                return {"Nome": nome, "Requisito": ferramenta}
            else:
                raise ValueError
        except ValueError:
                    print("Requisitos disponíveis: Kit unha, Kit cabelo e Kit pele. Para mais ferramentas contate o administrador.")
                    self.__controle.abre_tela()

    def mostra_dados_servico(self, nome: str, requisito: str):
        print("Serviço:", nome)
        print("Requisito:", requisito)

    def encontra_servico(self):
        print(" ---- Exclusão de Serviço ---- ")
        nome = input("Nome do serviço que deseja excluir: ")
        return nome

    def altera_dados_servico(self):
        print(" ---- Alteração de Serviço ----")
        try:
            nome_servico = input("Nome do servico a ser alterado: ")
            if nome_servico not in self.__controle.servicos_nome():
                raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.excecao(mensagem="Serviço não existe!")
            self.__controle.abre_tela()
        print("Dados: nome, requisito")
        try:
            dado = input("Dado a ser alterado: ")
            if dado == "requisito":
                try:
                    valor = input("Insira o " + dado + ": ")
                    if valor == "kit unha" or valor == "kit cabelo" or valor == "kit pele":
                        return nome_servico, dado, valor
                    else:
                        raise ValueError
                except ValueError:
                    print("Requisitos disponíveis: Kit unha, Kit cabelo e Kit pele. Para mais ferramentas contate o administrador")
                    self.__controle.abre_tela()
            elif dado == "nome":
                valor = input("Insira o " + dado + ": ")
            else:
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados válidos: nome, requisitos")
            self.__controle.abre_tela()
        return nome_servico, dado, valor

    def excecao(self, mensagem):
        print(mensagem)