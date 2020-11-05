class ClienteJaCadastrado(Exception):

    def __init__(self):
        super().__init__('Essa ferramenta já foi cadastrada.')