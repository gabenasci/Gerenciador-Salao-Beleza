class FuncionarioIndisponivelExcecao(Exception):

    def __init__(self):
        super().__init__('Este funcionário não está disponível no dia e hora desejados.')