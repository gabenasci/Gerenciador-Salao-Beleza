class ClienteNaoExisteExcecao(Exception):

    def __init__(self):
        super().__init__('Não existe um cliente cadastrado com esse nome.')