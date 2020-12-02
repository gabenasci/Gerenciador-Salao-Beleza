from DAO.abstract_DAO import DAO
from entidade.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        if (atendimento is not None) and (isinstance(atendimento.id, int)) and (isinstance(atendimento, Atendimento)):
            super().add(atendimento.id, atendimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)