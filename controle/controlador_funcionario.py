from limite.tela_funcionario import TelaFuncionario
from limite.tela_inclui_funcionario import TelaIncluiFuncionario
from entidade.funcionario import Funcionario
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado
import PySimpleGUI as sg
import datetime

class ControladorFuncionario:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__funcionarios = [Funcionario('Gabriel', datetime.date(1998, 7, 30), 48988096814, datetime.date(2020, 7, 30))]
        self.__controlador = controlador_sistema
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_inclui_funcionario = TelaIncluiFuncionario(self)
        self.__continua_exibindo_tela = True

    def __new__(cls, controlador_sistema):
        if ControladorFuncionario.__instance is None:
            ControladorFuncionario.__instance = object.__new__(cls)
        return ControladorFuncionario.__instance

    def abre_tela(self):

        switcher = {'Incluir': self.inclui_funcionario, 'Listar': self.lista_funcionarios,
                     'Voltar': self.retorna}

        #self.__continua_exibindo_tela = True
        #while self.__continua_exibindo_tela:
        while True:
            self.__tela_funcionario.init_components()
            button, values = self.__tela_funcionario.open()
            if button == 'Voltar' or button == sg.WIN_CLOSED:
                break
            elif button == 'Excluir':
                for funcionario in self.__funcionarios:
                    if values[funcionario.nome] == True:
                        self.__funcionarios.remove(funcionario)
            elif button == 'Alterar':
                for funcionario in self.__funcionarios:
                    if values[funcionario.nome] == True:
                        self.altera_funcionario()
            else:
                funcao_escolhida = switcher[button]
                funcao_escolhida()

            self.__tela_funcionario.close()
        self.__tela_funcionario.close()


    def inclui_funcionario(self):

        self.__tela_inclui_funcionario.init_components()
        button, values = self.__tela_inclui_funcionario.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_funcionario.close()

        if button == 'Salvar':

            nome = values["it_nome"]
            try:
                data = values["it_data_nascimento"]
                dia, mes, ano = map(int, data.split('/'))
                data_nascimento = datetime.date(ano, mes, dia)
            except ValueError:
                sg.Popup("Data inválida!")
                self.__controlador.abre_tela()
            telefone = values["it_telefone"]
            try:
                telefone = int(telefone)
            except ValueError:
                sg.Popup("Valor inteiro inválido!")
                self.__controlador.abre_tela()
            try:
                data2 = values["it_data_contratacao"]
                dia, mes, ano = map(int, data2.split('/'))
                data_contratacao = datetime.date(ano, mes, dia)
            except ValueError:
                sg.Popup("Data inválida!")
                self.__controlador.abre_tela()
            #dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
            #                     "data_contratacao": data_contratacao}
            try:
                for funcionario in self.__funcionarios:
                    if funcionario.nome == values["it_nome"]:
                        raise ObjetoJaCadastrado
                novo_funcionario = Funcionario(nome, data_nascimento, telefone, data_contratacao)
                self.__funcionarios.append(novo_funcionario)
                self.__tela_inclui_funcionario.close()
                sg.Popup('Funcionario Cadastrado')
            except ObjetoJaCadastrado:
                self.__tela_funcionario.excecao(mensagem="Já existe um funcionario cadastrado com esse nome! Por favor, cadastre novamente adicionando o sobrenome.")

        '''
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
        '''

    def altera_funcionario(self):
        self.__tela_inclui_funcionario.init_components()
        button, values = self.__tela_inclui_funcionario.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_funcionario.close()

        if button == 'Salvar':
            nome = values["it_nome"]
            try:
                data = values["it_data_nascimento"]
                dia, mes, ano = map(int, data.split('/'))
                data_nascimento = datetime.date(ano, mes, dia)
            except ValueError:
                sg.Popup("Data inválida!")
                self.__controlador.abre_tela()
            telefone = values["it_telefone"]
            try:
                telefone = int(telefone)
            except ValueError:
                sg.Popup("Valor inteiro inválido!")
                self.__controlador.abre_tela()
            try:
                data2 = values["it_data_contratacao"]
                dia, mes, ano = map(int, data2.split('/'))
                data_contratacao = datetime.date(ano, mes, dia)
            except ValueError:
                sg.Popup("Data inválida!")
                self.__controlador.abre_tela()
            # dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
            #                     "data_contratacao": data_contratacao}
            try:
                for funcionario in self.__funcionarios:
                    if funcionario.nome == values["it_nome"]:
                        raise ObjetoJaCadastrado
                self.__funcionarios.remove(funcionario)
                funcionario_alterado = Funcionario(nome, data_nascimento, telefone, data_contratacao)
                self.__funcionarios.append(funcionario_alterado)
                self.__tela_inclui_funcionario.close()
                sg.Popup('Funcionario Alterado')
            except ObjetoJaCadastrado:
                self.__tela_funcionario.excecao(
                    mensagem="Já existe um funcionario cadastrado com esse nome! Por favor, cadastre novamente adicionando o sobrenome.")

        '''
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
        '''
    def exclui_funcionario(self):
        button, values = self.__tela_funcionario.open()
        for funcionario in self.__funcionarios:
            if values[funcionario.nome] == True:
                self.__funcionarios.remove(funcionario)
        '''
        nome_funcionario = self.__tela_funcionario.encontra_funcionario()
        try:
            for obj in self.__funcionarios:
                if obj.nome == nome_funcionario:
                    self.__funcionarios.remove(obj)
                else:
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.__tela_funcionario.excecao(mensagem="Não existe nenhum funcionário com esse nome. Por favor, confira a lista de clientes cadastrados")
        '''
    def lista_funcionarios(self):
        for funcionario in self.__funcionarios:
            self.__tela_funcionario.mostra_dados_funcionario(funcionario.nome, funcionario.data_nascimento, funcionario.data_contratacao)

    def retorna(self):
        #self.__continua_exibindo_tela = False
        self.__tela_funcionario.close()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def funcionarios_nome(self):
        funcionarios_str = []
        for f in self.__funcionarios:
            funcionarios_str.append(f.nome)
        return funcionarios_str
