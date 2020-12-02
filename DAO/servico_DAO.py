from DAO.abstract_DAO import DAO
from entidade.servico import Servico

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__('servicos.pkl')

    def add(self, servico: Servico):
        if (servico is not None) and (isinstance(servico.nome, str)) and (isinstance(servico, Servico)):
            super().add(servico.nome, servico)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

