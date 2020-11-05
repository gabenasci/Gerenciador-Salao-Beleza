class AtendimentoNaoExisteExcecao(Exception):

    def __init__(self):
        super().__init__('Não existe um atendimento registrado com esse id.')