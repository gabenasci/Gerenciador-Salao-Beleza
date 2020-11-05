from excecoes.funcionario_indisponivel import FuncionarioIndisponivelExcecao
from excecoes.atendimento_nao_existe import AtendimentoNaoExisteExcecao
from entidade.atendimento import Atendimento
from limite.tela_atendimento import TelaAtendimento

class ControladorAtendimento:

    def __init__(self, controlador_sistema):
        self.__atendimentos = []
        self.__controlador = controlador_sistema
        self.__tela_atendimento = TelaAtendimento(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_atendimento, 2: self.exclui_atendimento, 3: self.altera_atendimentos, 4: self.lista_atendimentos_cliente, 5: self.lista_atendimentos_dia, 6: self.gera_relatorio_mes}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_atendimento.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_atendimento(self):
        dados_atendimento = self.__tela_atendimento.solicita_dados_atendimento()
        try:
            for obj in self.__atendimentos:
                if obj.funcionario == dados_atendimento["funcionario"] and obj.data == dados_atendimento["data"] and obj.hora == dados_atendimento["hora"]:
                    raise FuncionarioIndisponivelExcecao
            novo_atendimento = Atendimento(dados_atendimento["servico"], dados_atendimento["cliente"], dados_atendimento["funcionario"],
                                           dados_atendimento["data"], dados_atendimento["hora"], dados_atendimento["valor"], dados_atendimento["pago"])
            self.__atendimentos.append(novo_atendimento)
            novo_atendimento.id = len(self.__atendimentos)
        except FuncionarioIndisponivelExcecao:
            self.__tela_atendimento.excecao(mensagem="Este funcionário não está disponível no dia e hora desejados. Por favor, tente outro")

    def exclui_atendimento(self):
        id_atendimento = self.__tela_atendimento.encontra_atendimento()
        try:
            for obj in self.__atendimentos:
                if obj.id == id_atendimento:
                    self.__atendimentos.remove(obj)
                else:
                    raise AtendimentoNaoExisteExcecao
        except AtendimentoNaoExisteExcecao:
            self.__tela_atendimento.excecao(
                mensagem="Não existe nenhum atendimento registrado com esse id. Por favor, confira a lista de atendimentos registrados e tente novamente")

    def lista_atendimentos_cliente(self):
        cliente = self.__tela_atendimento.atendimento_cliente()
        for atendimento in self.__atendimentos:
            if atendimento.cliente == cliente:
                self.__tela_atendimento.mostra_dados_atendimento(atendimento.id, atendimento.servico,
                                                                 atendimento.cliente, atendimento.funcionario,
                                                                 atendimento.data, atendimento.hora,
                                                                 atendimento.valor, atendimento.pago)

    def lista_atendimentos_dia(self):
        dia = self.__tela_atendimento.atendimento_dia()
        for atendimento in self.__atendimentos:
            if atendimento.dia == dia:
                self.__tela_atendimento.mostra_dados_atendimento(atendimento.id, atendimento.servico,
                                                                 atendimento.cliente, atendimento.funcionario,
                                                                 atendimento.data, atendimento.hora,
                                                                 atendimento.valor, atendimento.pago)

    def altera_atendimentos(self):
        pass

    def gera_relatorio_mes(self):
        mes = self.__tela_atendimento.relatorio_mes()
        atendimentos_mes = []
        for atendimento in self.__atendimentos:
            if atendimento.data.datetime.date.month == mes:
                atendimentos_mes.append(atendimento.servico)
                for i in atendimentos_mes:
                    print(i)

    def retorna(self):
        self.__continua_exibindo_tela = False