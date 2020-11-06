class ObjetoJaCadastrado(Exception):

    def __init__(self):
        super().__init__('Já existe um objeto com este identificador no sistema.')