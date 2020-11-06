class ObjetoNaoExisteExcecao(Exception):

    def __init__(self):
        super().__init__('O registro procurado não existe.')