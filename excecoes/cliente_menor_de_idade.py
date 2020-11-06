class ClienteMenorDeIdade(Exception):

    def __init__(self):
        super().__init__('O cliente é menor de idade e não pode ser cadastrado.')