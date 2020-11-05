from limite.tela_servico import TelaServico
from entidade.servico import Servico
from entidade.atendimento import Atendimento

class ControladorServico:
    def __init__(self, controlador_sistema):
        self.__servicos = []

        self.__controlador = controlador_sistema
        self.__tela_servico = TelaServico(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_servico, 2: self.exclui_servico, 3: self.lista_servicos, 4: self.altera_servico, 5: self.habilita_funcionario}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_servico.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_servico(self):
        dados_servico = self.__tela_servico.solicita_dados_servico()
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

    def exclui_servico(self):
        nome_servico = self.__tela_servico.encontra_servico()
        for obj in self.__servicos:
            if obj.nome == nome_servico:
                if (obj is not None) and (isinstance(obj, Servico)):
                    self.__servicos.remove(obj)

    def lista_servicos(self):
        for servico in self.__servicos:
            self.__tela_servico.mostra_dados_servico(servico.nome, servico.requisito)

    def altera_servico(self):
        nome_servico, dado, valor_dado = self.__tela_servico.altera_dados_servico()
        for servico in self.__servicos:
            if servico.nome == nome_servico:
                dados_servico = {"nome": servico.nome,
                                     "requisito": servico.requisito}
                dados_servico[dado] = valor_dado
                self.__servicos.remove(servico)
                servico_alterado = Servico(dados_servico["nome"], dados_servico["requisito"])
                self.__servicos.append(servico_alterado)

    def habilita_funcionario(self):
        funcionario, servico = self.__tela_servico.encontra_funcionario()
        for f in self.__controlador.funcionarios():
            if f.nome == funcionario:
                print('passou funcionario')
                for s in self.__servicos:
                    print('passou servicos')
                    if s.nome == servico:
                        s.add_funcionario(f)
                        print("chamou a funcao")

    def retorna(self):
        self.__continua_exibindo_tela = False