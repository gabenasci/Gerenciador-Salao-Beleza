from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from excecoes.objeto_nao_existe import ObjetoNaoExisteExcecao
from excecoes.objeto_ja_cadastrado import ObjetoJaCadastrado
from excecoes.cliente_menor_de_idade import ClienteMenorDeIdade
from datetime import datetime

class ControladorCliente:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__clientes = []

        self.__controlador = controlador_sistema
        self.__tela_cliente = TelaCliente(self)
        self.__continua_exibindo_tela = True

    def __new__(cls, controlador_sistema):
        if ControladorCliente.__instance is None:
            ControladorCliente.__instance = object.__new__(cls)
        return ControladorCliente.__instance

    def abre_tela(self):
        switcher = {0: self.retorna, 1: self.inclui_cliente, 2: self.exclui_cliente, 3: self.lista_clientes, 4: self.altera_cliente}

        self.__continua_exibindo_tela = True
        while self.__continua_exibindo_tela:
            opcao = self.__tela_cliente.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.solicita_dados_cliente()
        try:
            for obj in self.__clientes:
                if obj.nome == dados_cliente["Nome"]:
                    raise ObjetoJaCadastrado
            if datetime.now().year - dados_cliente["Data_nascimento"].year < 18:
                raise ClienteMenorDeIdade
            novo_cliente = Cliente(dados_cliente["Nome"], dados_cliente["Data_nascimento"], dados_cliente["Telefone"], dados_cliente["Instagram"], dados_cliente["Tipo_cliente"], dados_cliente["Obs"])
            self.__clientes.append(novo_cliente)
        except ObjetoJaCadastrado:
            self.__tela_cliente.excecao(mensagem="Já existe um cliente cadastrado com esse nome! Por favor, cadastre novamente adicionando o sobrenome.")
        except ClienteMenorDeIdade:
            self.__tela_cliente.excecao(mensagem="O cliente que está tentando cadastrar é menor de idade. Cadastre um responsável e adicione o nome do menor nas observações.")

    def exclui_cliente(self):
        nome_cliente = self.__tela_cliente.encontra_cliente()
        try:
            for obj in self.__clientes:
                if obj.nome == nome_cliente:
                    self.__clientes.remove(obj)
                else:
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao:
            self.__tela_cliente.excecao(mensagem="Não existe nenhum cliente com esse nome. Por favor, confira a lista de clientes cadastrados")

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_dados_cliente(cliente.nome, cliente.telefone, cliente.data_nascimento, cliente.instagram, cliente.tipo_cliente, cliente.obs)

    def altera_cliente(self):
        nome_cliente, dado, valor_dado = self.__tela_cliente.altera_dados_cliente()
        try:
            for cliente in self.__clientes:
                if cliente.nome == nome_cliente:
                    dados_cliente = {"nome": cliente.nome, "data_nascimento": cliente.data_nascimento, "telefone": cliente.telefone,
                                     "instagram": cliente.instagram, "tipo_cliente": cliente.tipo_cliente, "obs": cliente.obs}
                    dados_cliente[dado] = valor_dado
                    self.__clientes.remove(cliente)
                    cliente_alterado = Cliente(dados_cliente["nome"], dados_cliente["data_nascimento"], dados_cliente["telefone"],
                                           dados_cliente["instagram"], dados_cliente["tipo_cliente"], dados_cliente["obs"])
                    self.__clientes.append(cliente_alterado)
                else:
                    raise ObjetoNaoExisteExcecao
        except ObjetoNaoExisteExcecao: self.__tela_cliente.excecao(mensagem="Não existe nenhum cliente com esse nome. Por favor, confira a lista de clientes cadastrados")

    def retorna(self):
        self.__continua_exibindo_tela = False

    @property
    def clientes(self):
        return self.__clientes

    def clientes_nome(self):
        clientes_str = []
        for c in self.__clientes:
            clientes_str.append(c.nome)
        return clientes_str