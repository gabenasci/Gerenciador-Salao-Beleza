from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from DAO.ClienteDAO import ClienteDAO
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado
from excecoes.cliente_menor_de_idade import ClienteMenorDeIdade
from excecoes.campo_nao_preenchido import CampoNaoPreenchido
import datetime as dt
from datetime import datetime
from limite.tela_inclui_cliente import TelaIncluiCliente
import PySimpleGUI as sg

class ControladorCliente:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__cliente_dao = ClienteDAO()
        self.__controlador = controlador_sistema
        self.__tela_cliente = TelaCliente(self)
        self.__tela_inclui_cliente = TelaIncluiCliente(self)
        self.__continua_exibindo_tela = True

    def __new__(cls, controlador_sistema):
        if ControladorCliente.__instance is None:
            ControladorCliente.__instance = object.__new__(cls)
        return ControladorCliente.__instance

    def abre_tela(self):
        switcher = {'Incluir': self.inclui_cliente, 'Listar': self.lista_clientes, 'Voltar': self.retorna}

        while True:
            self.__tela_cliente.init_components()
            button, values = self.__tela_cliente.open()
            if button == 'Voltar' or button == sg.WIN_CLOSED:
                break
            elif button == 'Excluir':
                for cliente in self.__cliente_dao.get_all():
                    if values[cliente.nome] == True:
                        self.__cliente_dao.remove(cliente.nome)
            elif button == 'Alterar':
                for cliente in self.__cliente_dao.get_all():
                    if values[cliente.nome] == True:
                        ano_n = str(cliente.data_nascimento.year)
                        mes_n = str(cliente.data_nascimento.month)
                        dia_n = str(cliente.data_nascimento.day)
                        data_n = dia_n + '/' + mes_n + '/' + ano_n
                        self.altera_cliente(cliente.nome, data_n,
                                                cliente.telefone, cliente.instagram, cliente.tipo_cliente, cliente.obs)
            else:
                funcao_escolhida = switcher[button]
                if funcao_escolhida == self.inclui_cliente:
                    self.inclui_cliente(None, None, None, None, None, None)
            self.__tela_cliente.close()
        self.__tela_cliente.close()

    def inclui_cliente(self, nome, data_n, telefone, instagram, tipo_cliente, obs):
        self.__tela_inclui_cliente.init_components(nome, data_n, telefone, instagram, tipo_cliente, obs)
        button, values = self.__tela_inclui_cliente.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_cliente.close()
        cadastro = True
        if button == 'Salvar':
            while cadastro:
                nome = values['it_nome']
                try:
                    data = values['it_data_nascimento']
                    dia, mes, ano = map(int, data.split('/'))
                    data_nascimento = dt.date(ano, mes, dia)
                    try:
                        idade = datetime.now().year - data_nascimento.year
                        if idade < 18:
                            raise ClienteMenorDeIdade
                    except ClienteMenorDeIdade:
                        sg.Popup("Cliente menor de idade!")
                        self.__tela_inclui_cliente.close()
                        self.inclui_cliente(values['it_nome'], None, values['it_telefone'], values['it_instagram'],
                                            tipo_cliente, values['it_obs'])
                        break
                except ValueError:
                    sg.Popup("Data de nascimento inválida!")
                    self.__tela_inclui_cliente.close()
                    self.inclui_cliente(values['it_nome'], None, values['it_telefone'], values['it_instagram'], values['it_tipo_cliente'], values['it_obs'])
                    break
                telefone = values['it_telefone']
                try:
                    telefone = int(telefone)
                except ValueError:
                    sg.Popup("Digite um telefone válido! Apenas números inteiros.")
                    self.__tela_inclui_cliente.close()
                    self.inclui_cliente(values['it_nome'], values['it_data_nascimento'], None, values['it_instagram'], values['it_tipo_cliente'], values['it_obs'])
                    break
                instagram = values['it_instagram']
                try:
                    if values['it_tipo_cliente1']:
                        tipo_cliente = 'Ouro'
                    elif values['it_tipo_cliente2']:
                        tipo_cliente = 'Prata'
                    elif values['it_tipo_cliente3']:
                        tipo_cliente = 'Bronze'
                    elif tipo_cliente == None:
                        raise CampoNaoPreenchido
                except CampoNaoPreenchido:
                    sg.Popup('Escolha um tipo para o cliente!')
                    self.__tela_inclui_cliente.close()
                    self.inclui_cliente(values['it_nome'], values['it_data_nascimento'], values['it_telefone'], values['it_instagram'], None, values['it_obs'])
                    break
                obs = values['it_obs']
                try:
                    for cliente in self.__cliente_dao.get_all():
                        if cliente.nome == values["it_nome"]:
                            raise ObjetoJaCadastrado
                    novo_cliente = Cliente(nome, data_nascimento, telefone, instagram, tipo_cliente, obs)
                    self.__cliente_dao.add(novo_cliente)
                    self.__tela_inclui_cliente.close()
                    sg.Popup('Cliente cadastrado!')
                    cadastro = False
                    break
                except ObjetoJaCadastrado:
                    sg.Popup('Já existe um cliente com esse nome! Adicione o sobrenome ou um identificador')
                    self.__tela_inclui_cliente.close()
                    self.inclui_cliente(None, values['it_data_nascimento'], values['it_telefone'], values['it_instagram'], tipo_cliente, values['it_obs'])
                    break


    #def inclui_cliente(self):
        #dados_cliente = self.__tela_cliente.solicita_dados_cliente()
        #try:
            #for obj in self.__clientes:
                #if obj.nome == dados_cliente["Nome"]:
                    #raise ObjetoJaCadastrado
            #if datetime.now().year - dados_cliente["Data_nascimento"].year < 18:
                #raise ClienteMenorDeIdade
            #novo_cliente = Cliente(dados_cliente["Nome"], dados_cliente["Data_nascimento"], dados_cliente["Telefone"], dados_cliente["Instagram"], dados_cliente["Tipo_cliente"], dados_cliente["Obs"])
            #self.__clientes.append(novo_cliente)
        #except ObjetoJaCadastrado:
            #self.__tela_cliente.excecao(mensagem="Já existe um cliente cadastrado com esse nome! Por favor, cadastre novamente adicionando o sobrenome.")
        #except ClienteMenorDeIdade:
            #self.__tela_cliente.excecao(mensagem="O cliente que está tentando cadastrar é menor de idade. Cadastre um responsável e adicione o nome do menor nas observações.")


    def exclui_cliente(self):
        button, values = self.__tela_cliente.open()
        for cliente in self.__cliente_dao.get_all():
            if values[cliente.nome] == True:
                self.__cliente_dao.remove(cliente.nome)


    def lista_clientes(self):
        for cliente in self.__cliente_dao.get_all():
            self.__tela_cliente.mostra_dados_cliente(cliente.nome, cliente.telefone, cliente.data_nascimento, cliente.instagram, cliente.tipo_cliente, cliente.obs)

    def altera_cliente(self, nome, data_n, telefone, instagram, tipo_cliente, obs):
        self.__tela_inclui_cliente.init_components(nome, data_n, telefone, instagram, tipo_cliente, obs)
        button, values = self.__tela_inclui_cliente.open()
        if button == sg.WIN_CLOSED or button == 'Voltar':
            self.__tela_inclui_cliente.close()

        cadastro = True
        if button == 'Salvar':
            while cadastro:
                self.__cliente_dao.remove(nome)
                nome = values['it_nome']
                try:
                    data = values["it_data_nascimento"]
                    dia, mes, ano = map(int, data.split('/'))
                    data_nascimento = dt.date(ano, mes, dia)
                    try:
                        idade = datetime.now().year - data_nascimento.year
                        if idade < 18:
                            raise ClienteMenorDeIdade
                    except ClienteMenorDeIdade:
                        sg.Popup("Cliente menor de idade!")
                        self.__tela_inclui_cliente.close()
                        self.inclui_cliente(values['it_nome'], None, values['it_telefone'], values['it_instagram'],
                                            tipo_cliente, values['it_obs'])
                        break
                except ValueError:
                    sg.Popup("Data inválida!")
                    self.__tela_inclui_cliente.close()
                    self.altera_cliente()
                    break
                telefone = values['it_telefone']
                try:
                    telefone = int(telefone)
                except ValueError:
                    sg.Popup("Valor inteiro inválido!")
                    self.__tela_inclui_cliente.close()
                    self.altera_cliente()
                    break
                instagram = values['it_instagram']
                try:
                    if values['it_tipo_cliente1']:
                        tipo_cliente = 'Ouro'
                    elif values['it_tipo_cliente2']:
                        tipo_cliente = 'Prata'
                    elif values['it_tipo_cliente3']:
                        tipo_cliente = 'Bronze'
                    elif tipo_cliente == None:
                        raise CampoNaoPreenchido
                except CampoNaoPreenchido:
                    sg.Popup('Escolha um tipo para o cliente!')
                    self.__tela_inclui_cliente.close()
                    self.altera_cliente()
                obs = values['it_obs']
                cliente_alterado = Cliente(nome, data_nascimento, telefone, instagram, tipo_cliente, obs)
                self.__cliente_dao.add(cliente_alterado)
                self.__tela_inclui_cliente.close()
                sg.Popup('Cliente foi alterado!')
                cadastro = False
                break

    def retorna(self):
        self.__tela_cliente.close()

    @property
    def clientes(self):
        return self.__cliente_dao.get_all()

    def clientes_nome(self):
        clientes_str = []
        for cliente in self.__cliente_dao.get_all():
            clientes_str.append(cliente.nome)
        return clientes_str

