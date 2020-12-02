from limite.tela_servico import TelaServico
from entidade.servico import Servico
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado
from DAO.servico_DAO import ServicoDAO
from limite.tela_inclui_servico import TelaIncluiServico
import PySimpleGUI as sg


class ControladorServico:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__servico_dao = ServicoDAO()
        #self.__servicos = [Servico('Teste', 'Nenhum')]
        self.__controlador = controlador_sistema
        self.__tela_servico = TelaServico(self)
        self.__tela_inclui_servico = TelaIncluiServico(self)
        self.__continua_exibindo_tela = True

    def __new__(cls, controlador_sistema):
        if ControladorServico.__instance is None:
            ControladorServico.__instance = object.__new__(cls)
        return ControladorServico.__instance

    def abre_tela(self):
        switcher = {'Incluir': self.inclui_servico, 'Listar': self.lista_servicos, 'Voltar': self.retorna}

        #self.__continua_exibindo_tela = True
        #while self.__continua_exibindo_tela:
        while True:
            self.__tela_servico.init_components()
            button, values = self.__tela_servico.open()
            if button == 'Voltar' or button == sg.WIN_CLOSED:
                break
            elif button == 'Excluir':
                for servico in self.__servico_dao.get_all():
                    if values[servico.nome] == True:
                        self.__servico_dao.remove(servico.nome)
            else:
                funcao_escolhida = switcher[button]
                if funcao_escolhida == self.inclui_servico:
                    self.inclui_servico(None, None)
            self.__tela_servico.close()
        self.__tela_servico.close()

    def inclui_servico(self, nome, requisito):
        self.__tela_inclui_servico.init_components(nome, requisito)
        button, values = self.__tela_inclui_servico.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_servico.close()
        cadastro = True
        if button == 'Salvar':
            while cadastro:
                nome = values['it_nome']
                requisito = values['it_requisito']
                try:
                    for servico in self.__servico_dao.get_all():
                        if servico.nome == values["it_nome"]:
                            raise ObjetoJaCadastrado
                    novo_servico = Servico(nome, requisito)
                    self.__servico_dao.add(novo_servico)
                    self.__tela_inclui_servico.close()
                    sg.Popup('Servico cadastrado!')
                    cadastro = False
                    break
                except ObjetoJaCadastrado:
                    sg.Popup('Já existe um serviço com esse nome!')
                    self.__tela_inclui_servico.close()
                    self.inclui_servico()
                    break

    def exclui_servico(self):
        button, values = self.__tela_servico.open()
        for servico in self.__servico_dao.get_all():
            if values[servico.nome] == True:
                self.__servico_dao.remove(servico.nome)

    def lista_servicos(self):
        for servico in self.__servico_dao.get_all():
            self.__tela_servico.mostra_dados_servico(servico.nome, servico.requisito)

    def retorna(self):
        self.__continua_exibindo_tela = False

    @property
    def servicos(self):
        return self.__servico_dao.get_all()

    def servicos_nome(self):
        servicos_str = []
        for s in self.__servico_dao.get_all():
            servicos_str.append(s.nome)
        return servicos_str

    def busca_servico_nome(self, nome_servico):
        for servico in self.__servico_dao.get_all():
            if servico.nome == nome_servico:
                return nome_servico

