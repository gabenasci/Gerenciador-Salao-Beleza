from limite.tela_servico import TelaServico
from entidade.servico import Servico

class ControladorServico:
    def __init__(self, controlador_sistema):
        self.__servicos = []

        self.__controlador = controlador_sistema
        self.__tela_servico = TelaServico(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_servico, 2: self.exclui_servico, 3: self.lista_servicos, 4: self.altera_servico}

        while self.__continua_exibindo_tela:
            opcao = self.__tela_servico.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_servico(self):
        dados_servico = self.__tela_servico.solicita_dados_servico()
        novo_servico = Servico(dados_servico["Nome"], dados_servico["Contra_indic"])
        if (novo_servico is not None) and (isinstance(novo_servico, Servico)):
            if novo_servico not in self.__servicos:
                self.__servicos.append(novo_servico)

    def exclui_servico(self):
        nome_servico = self.__tela_servico.encontra_servico()
        for obj in self.__servicos:
            if obj.nome == nome_servico:
                if (obj is not None) and (isinstance(obj, Servico)):
                    self.__servicos.remove(obj)

    def lista_servicos(self):
        for servico in self.__servicos:
            self.__tela_servico.mostra_dados_servico(servico.nome)

    def altera_servico(self):
        pass

    def habilita_funcionario(self):
        pass


    def retorna(self):
        self.__continua_exibindo_tela = False