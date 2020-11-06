from excecoes.funcionario_indisponivel import FuncionarioIndisponivelExcecao
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from entidade.atendimento import Atendimento
from limite.tela_atendimento import TelaAtendimento
from collections import Counter


class ControladorAtendimento:

    def __init__(self, controlador_sistema):
        self.__atendimentos = []
        self.__controlador = controlador_sistema
        self.__tela_atendimento = TelaAtendimento(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_atendimento, 2: self.exclui_atendimento, 3: self.altera_atendimento,
                    4: self.lista_atendimentos_cliente, 5: self.lista_atendimentos_dia, 6: self.gera_relatorio_mes}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_atendimento.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_atendimento(self):
        dados_atendimento = self.__tela_atendimento.solicita_dados_atendimento()
        try:
            for obj in self.__atendimentos:
                if obj.funcionario == dados_atendimento["funcionario"] and obj.data == dados_atendimento["data"] and \
                        obj.hora == dados_atendimento["hora"]:
                    raise FuncionarioIndisponivelExcecao
            for s in self.__controlador.servicos():
                if s.nome == dados_atendimento["servico"]:
                    dados_atendimento["servico"] = s
            for c in self.__controlador.clientes():
                if c.nome == dados_atendimento["cliente"]:
                    dados_atendimento["cliente"] = c
            for f in self.__controlador.funcionarios():
                if f.nome == dados_atendimento["funcionario"]:
                    dados_atendimento["funcionario"] = f
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
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.__tela_atendimento.excecao(
                mensagem="Não existe nenhum atendimento registrado com esse id. Por favor, confira a lista de atendimentos registrados e tente novamente")

    def lista_atendimentos_cliente(self):
        cliente = self.__tela_atendimento.atendimento_cliente()
        for atendimento in self.__atendimentos:
            if atendimento.cliente.nome == cliente:
                self.__tela_atendimento.mostra_dados_atendimento(atendimento.id, atendimento.servico,
                                                                 atendimento.cliente, atendimento.funcionario,
                                                                atendimento.data, atendimento.hora, atendimento.valor,
                                                                atendimento.pago)

    def lista_atendimentos_dia(self):
        dia = self.__tela_atendimento.atendimento_dia()
        for atendimento in self.__atendimentos:
            if atendimento.data == dia:
                self.__tela_atendimento.mostra_dados_atendimento(atendimento.id, atendimento.servico,
                                                                 atendimento.cliente, atendimento.funcionario,
                                                                 atendimento.data, atendimento.hora,
                                                                 atendimento.valor, atendimento.pago)
    def altera_atendimento(self):
        id_atendimento, dado, valor_dado = self.__tela_atendimento.altera_dados_atendimento()
        for atendimento in self.__atendimentos:
            if atendimento.id == id_atendimento:
                dados_atendimento = {"servico": atendimento.servico,
                                     "cliente": atendimento.cliente,
                                     "funcionario": atendimento.funcionario, "data": atendimento.data,
                                     "hora": atendimento.hora, "valor": atendimento.valor,
                                     "pago": atendimento.pago}
                dados_atendimento[dado] = valor_dado
                for s in self.__controlador.servicos():
                    if s.nome == dados_atendimento["servico"]:
                        dados_atendimento["servico"] = s
                for c in self.__controlador.clientes():
                    if c.nome == dados_atendimento["cliente"]:
                        dados_atendimento["cliente"] = c
                for f in self.__controlador.funcionarios():
                    if f.nome == dados_atendimento["funcionario"]:
                        dados_atendimento["funcionario"] = f
                self.__atendimentos.remove(atendimento)
                atendimento_alterado = Atendimento(dados_atendimento["servico"],
                                                   dados_atendimento["cliente"],
                                                   dados_atendimento["funcionario"], dados_atendimento["data"],
                                                   dados_atendimento["hora"], dados_atendimento["valor"],
                                                   dados_atendimento["pago"])
                self.__atendimentos.append(atendimento_alterado)
                atendimento_alterado.id = len(self.__atendimentos)

    def gera_relatorio_mes(self):
        mes = self.__tela_atendimento.relatorio_mes()
        atendimentos_mes = []
        for atendimento in self.__atendimentos:
            if atendimento.data.month == mes:
                atendimentos_mes.append(atendimento.servico.nome)
        contador_servicos = dict(Counter(atendimentos_mes))
        print("--- Número de atendimentos no mês "+str(mes)+": ---")
        for chave, valor in contador_servicos.items():
            print(chave+':', valor)

    def retorna(self):
        self.__continua_exibindo_tela = False