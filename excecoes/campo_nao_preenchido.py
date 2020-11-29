class CampoNaoPreenchido(Exception):

    def __init__(self):
        super().__init__('Algum campo essencial não foi preenchido.')