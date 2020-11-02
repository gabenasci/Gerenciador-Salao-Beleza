class ClienteJaCadastrado(Exception):

    def __init__(self):
        super().__init__('Já existe um cliente com esse nome. Por favor, adicione o sobrenome ou um identificador')