from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado

class ControladorFuncionario:

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__controlador = controlador_sistema
        self.__tela_funcionario = TelaFuncionario(self)
        self.__continua_exibindo_tela = True

    def abre_tela(self):

        switcher = {0: self.retorna, 1: self.inclui_funcionario, 2: self.exclui_funcionario, 3: self.lista_funcionarios,
                    4: self.altera_funcionario, 5: self.habilita_funcionario}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_funcionario.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_funcionario(self):
        dados_funcionario = self.__tela_funcionario.solicita_dados_funcionario()
        try:
            for obj in self.__funcionarios:
                if obj.nome == dados_funcionario["Nome"]:
                    raise ObjetoJaCadastrado
            novo_funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["data_nascimento"],
                                           dados_funcionario["telefone"], dados_funcionario["data_contratacao"])
            self.__funcionarios.append(novo_funcionario)
        except ObjetoJaCadastrado:
            self.__tela_funcionario.excecao(mensagem="Já existe um funcionario cadastrado com esse nome! Por favor, cadastre novamente adicionando o sobrenome.")

    def altera_funcionario(self):
        nome_funcionario, dado, valor_dado = self.__tela_funcionario.altera_dados_funcionario()
        for funcionario in self.__funcionarios:
            if funcionario.nome == nome_funcionario:
                dados_funcionario = {"nome": funcionario.nome, "data_nascimento": funcionario.data_nascimento, "telefone": funcionario.telefone,
                                     "data_contratacao": funcionario.data_contratacao}
                dados_funcionario[dado] = valor_dado
                self.__funcionarios.remove(funcionario)
                funcionario_alterado = Funcionario(dados_funcionario["nome"], dados_funcionario["data_nascimento"],
                                       dados_funcionario["telefone"], dados_funcionario["data_contratacao"])
                self.__funcionarios.append(funcionario_alterado)

    def exclui_funcionario(self):
        nome_funcionario = self.__tela_funcionario.encontra_funcionario()
        try:
            for obj in self.__funcionarios:
                if obj.nome == nome_funcionario:
                    self.__funcionarios.remove(obj)
                else:
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.__tela_funcionario.excecao(mensagem="Não existe nenhum funcionário com esse nome. Por favor, confira a lista de clientes cadastrados")

    def lista_funcionarios(self):
        for funcionario in self.__funcionarios:
            self.__tela_funcionario.mostra_dados_funcionario(funcionario.nome, funcionario.data_nascimento, funcionario.data_contratacao)

    def retorna(self):
        self.__continua_exibindo_tela = False

    @property
    def funcionarios(self):
        return self.__funcionarios

    def funcionarios_nome(self):
        funcionarios_str = []
        for f in self.__funcionarios:
            funcionarios_str.append(f.nome)
        return funcionarios_str

    def habilita_funcionario(self):
        funcionario, servico = self.__tela_funcionario.encontra_servico()
        for f in self.__controlador.funcionarios():
            if f.nome == funcionario:
                print('passou funcionario')
                for s in self.__servicos:
                    print('passou servicos')
                    if s.nome == servico:
                        s.add_funcionario(f)
                        print("chamou a funcao")
