from limite.tela_funcionario import TelaFuncionario
from limite.tela_inclui_funcionario import TelaIncluiFuncionario
from entidade.funcionario import Funcionario
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado
import PySimpleGUI as sg
import datetime
from DAO.FuncionarioDAO import FuncionarioDAO

class ControladorFuncionario:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__funcionario_dao = FuncionarioDAO()

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
                for funcionario in self.__funcionario_dao.get_all():
                    # verifica se checkbox está clicado
                    if values[funcionario.nome] == True:
                        self.__funcionario_dao.remove(funcionario.nome)
            elif button == 'Alterar':
                for funcionario in self.__funcionario_dao.get_all():
                    if values[funcionario.nome] == True:
                        ano_n = str(funcionario.data_nascimento.year)
                        mes_n = str(funcionario.data_nascimento.month)
                        dia_n = str(funcionario.data_nascimento.day)
                        data_n = dia_n+'/'+mes_n+'/'+ano_n
                        ano_c = str(funcionario.data_contratacao.year)
                        mes_c = str(funcionario.data_contratacao.month)
                        dia_c = str(funcionario.data_contratacao.day)
                        data_c = dia_c+'/'+mes_c+'/'+ano_c
                        self.altera_funcionario(funcionario.nome, data_n,
                                                funcionario.telefone, data_c)
            else:
                funcao_escolhida = switcher[button]
                if funcao_escolhida == self.inclui_funcionario:
                    funcao_escolhida(None, None, None, None)

            self.__tela_funcionario.close()
        self.__tela_funcionario.close()


    def inclui_funcionario(self, nome, data_n, telefone, data_c):
        self.__tela_inclui_funcionario.init_components(nome, data_n, telefone, data_c)
        button, values = self.__tela_inclui_funcionario.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_funcionario.close()

        cadastro = True
        if button == 'Salvar':
            while cadastro:
                nome = values["it_nome"]
                try:
                    data = values["it_data_nascimento"]
                    dia, mes, ano = map(int, data.split('/'))
                    data_nascimento = datetime.date(ano, mes, dia)
                except ValueError:
                    sg.Popup("Data de nascimento inválida!")
                    self.__tela_inclui_funcionario.close()
                    self.inclui_funcionario(values['it_nome'], None, values['it_telefone'], values['it_data_contratacao'])
                    break
                telefone = values["it_telefone"]
                try:
                    telefone = int(telefone)
                except ValueError:
                    sg.Popup("Telefone inválido!")
                    self.__tela_inclui_funcionario.close()
                    self.inclui_funcionario(values['it_nome'], values["it_data_nascimento"], None, values['it_data_contratacao'])
                    break
                try:
                    data2 = values["it_data_contratacao"]
                    dia, mes, ano = map(int, data2.split('/'))
                    data_contratacao = datetime.date(ano, mes, dia)
                except ValueError:
                    sg.Popup("Data de contratação inválida!")
                    self.__tela_inclui_funcionario.close()
                    self.inclui_funcionario(values['it_nome'], values['it_data_nascimento'], values["it_telefone"], None)
                    break
                #dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                #                     "data_contratacao": data_contratacao}
                try:
                    for funcionario in self.__funcionario_dao.get_all():
                        if funcionario.nome == values["it_nome"]:
                            raise ObjetoJaCadastrado
                    novo_funcionario = Funcionario(nome, data_nascimento, telefone, data_contratacao)
                    self.__funcionario_dao.add(novo_funcionario)
                    self.__tela_inclui_funcionario.close()
                    sg.Popup('Funcionario Cadastrado')
                    cadastro = False
                    break
                except ObjetoJaCadastrado:
                    sg.Popup('Já existe um funcionário com esse nome!')
                    self.__tela_inclui_funcionario.close()
                    self.inclui_funcionario()
                    break

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

    def altera_funcionario(self, nome, data_n, telefone, data_c):
        self.__tela_inclui_funcionario.init_components(nome, data_n, telefone, data_c)
        button, values = self.__tela_inclui_funcionario.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_funcionario.close()

        cadastro = True
        if button == 'Salvar':
            while cadastro:
                nome = values["it_nome"]
                try:
                    data = values["it_data_nascimento"]
                    dia, mes, ano = map(int, data.split('/'))
                    data_nascimento = datetime.date(ano, mes, dia)
                except ValueError:
                    sg.Popup("Data inválida!")
                    self.__tela_inclui_funcionario.close()
                    self.altera_funcionario()
                    break
                telefone = values["it_telefone"]
                try:
                    telefone = int(telefone)
                except ValueError:
                    sg.Popup("Valor inteiro inválido!")
                    self.__tela_inclui_funcionario.close()
                    self.altera_funcionario()
                    break
                try:
                    data2 = values["it_data_contratacao"]
                    dia, mes, ano = map(int, data2.split('/'))
                    data_contratacao = datetime.date(ano, mes, dia)
                except ValueError:
                    sg.Popup("Data inválida!")
                    self.__tela_inclui_funcionario.close()
                    self.altera_funcionario()
                    break
                # dados_funcionario = {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                #                     "data_contratacao": data_contratacao}
                for funcionario in self.__funcionario_dao.get_all():
                    self.__funcionario_dao.remove(funcionario)
                funcionario_alterado = Funcionario(nome, data_nascimento, telefone, data_contratacao)
                self.__funcionario_dao.add(funcionario_alterado)
                self.__tela_inclui_funcionario.close()
                sg.Popup('Funcionario Alterado')
                cadastro = False
                break

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
        for funcionario in self.__funcionario_dao.get_all():
            if values[funcionario.nome] == True:
                self.__funcionario_dao.remove(funcionario.nome)
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
        for funcionario in self.__funcionario_dao.get_all():
            self.__tela_funcionario.mostra_dados_funcionario(funcionario.nome, funcionario.data_nascimento, funcionario.data_contratacao)

    def retorna(self):
        #self.__continua_exibindo_tela = False
        self.__tela_funcionario.close()

    @property
    def funcionarios(self):
        return self.__funcionario_dao.get_all()

    def funcionarios_nome(self):
        funcionarios_str = []
        for f in self.__funcionario_dao.get_all():
            funcionarios_str.append(f.nome)
        return funcionarios_str
