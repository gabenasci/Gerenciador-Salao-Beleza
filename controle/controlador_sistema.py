from limite.tela_sistema import TelaSistema


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def opcao_funcionarios(self):
        pass

    def opcao_clientes(self):
        pass

    def opcao_servicos(self):
        pass

    def opcao_atendimentos(self):
        pass

    def opcao_encerra(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.opcao_funcionarios, 2: self.opcao_clientes,
                        3: self.opcao_servicos, 4: self.opcao_atendimentos,
                        0: self.opcao_encerra}

        opcao_escolhida = self.__tela_sistema.tela_opcoes()

        funcao_escolhida = lista_opcoes[opcao_escolhida]

        funcao_escolhida()