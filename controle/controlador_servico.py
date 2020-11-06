from limite.tela_servico import TelaServico
from entidade.servico import Servico
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado


class ControladorServico:
    def __init__(self, controlador_sistema):
        self.__servicos = []

        self.__controlador = controlador_sistema
        self.__tela_servico = TelaServico(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_servico, 2: self.exclui_servico, 3: self.lista_servicos,
                    4: self.altera_servico}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_servico.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_servico(self):
        dados_servico = self.__tela_servico.solicita_dados_servico()
        try:
            if dados_servico["Requisito"] == Servico.kit_unha.nome:
                dados_servico["Requisito"] = Servico.kit_unha
            if dados_servico["Requisito"] == Servico.kit_cabelo.nome:
                dados_servico["Requisito"] = Servico.kit_cabelo
            if dados_servico["Requisito"] == Servico.kit_pele.nome:
                dados_servico["Requisito"] = Servico.kit_pele

            novo_servico = Servico(dados_servico["Nome"], dados_servico["Requisito"])
            if (novo_servico is not None) and (isinstance(novo_servico, Servico)):
                if novo_servico not in self.__servicos:
                    self.__servicos.append(novo_servico)
        except ObjetoJaCadastrado:
            self.__tela_servico.excecao(mensagem="Já existe um serviço cadastrado com esse nome! Por favor, verifique a lista de serviços cadastrados")

    def exclui_servico(self):
        nome_servico = self.__tela_servico.encontra_servico()
        try:
            for obj in self.__servicos:
                if obj.nome == nome_servico:
                    self.__servicos.remove(obj)
                else:
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.__tela_servico.excecao(mensagem="Não existe nenhum serviço com esse nome. Por favor, confira a lista de serviços cadastrados")

    def lista_servicos(self):
        for servico in self.__servicos:
            self.__tela_servico.mostra_dados_servico(servico.nome, servico.requisito)

    def altera_servico(self):
        nome_servico, dado, valor_dado = self.__tela_servico.altera_dados_servico()
        for servico in self.__servicos:
            if servico.nome == nome_servico:
                dados_servico = {"nome": servico.nome, "requisito": servico.requisito}
                dados_servico[dado] = valor_dado
                self.__servicos.remove(servico)
                servico_alterado = Servico(dados_servico["nome"], dados_servico["requisito"])
                self.__servicos.append(servico_alterado)

    def retorna(self):
        self.__continua_exibindo_tela = False

    @property
    def servicos(self):
        return self.__servicos

    def servicos_nome(self):
        servicos_str = []
        for s in self.__servicos:
            servicos_str.append(s.nome)
        return servicos_str