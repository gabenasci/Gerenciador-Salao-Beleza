from DAO.abstract_DAO import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (funcionario is not None) and (isinstance(funcionario.nome, str)) and (isinstance(funcionario, Funcionario)):
            super().add(funcionario.nome, funcionario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

