from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario


class ControladorFuncionario:

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__controlador = controlador_sistema
        self.__tela_funcionario = TelaFuncionario(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):

        switcher = {0: self.retorna, 1: self.inclui_funcionario, 3: self.lista_funcionarios}

        while self.__continua_exibindo_tela:
            opcao = self.__tela_funcionario.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_funcionario(self):
        dados_funcionario = self.__tela_funcionario.solicita_dados_funcionario()
        novo_funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["data_nascimento"],
                                       dados_funcionario["telefone"], dados_funcionario["data_contratacao"],
                                       dados_funcionario["servico"])
        self.__funcionarios.append(novo_funcionario)

    def lista_funcionarios(self):
        for funcionario in self.__funcionarios:
            self.__tela_funcionario.mostra_dados_funcionario(funcionario.nome)

    def retorna(self):
        self.__continua_exibindo_tela = False
