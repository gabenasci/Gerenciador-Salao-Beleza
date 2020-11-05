class Pagamento:

    def __init__(self, valor: float, pago: bool):
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(pago, bool):
            self.__pago = pago

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, pago: bool):
        if isinstance(pago, bool):
            self.__pago = pago