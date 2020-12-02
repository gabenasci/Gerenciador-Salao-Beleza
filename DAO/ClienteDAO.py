from DAO.abstract_DAO import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (cliente is not None) and (isinstance(cliente.nome, str)) and isinstance(cliente, Cliente):
            super().add(cliente.nome, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
