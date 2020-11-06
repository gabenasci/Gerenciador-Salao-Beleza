from entidade.ferramenta import Ferramenta

class Servico:
    def __init__(self, nome: str, requisito: Ferramenta):
        self.__nome = nome
        self.__funcionarios = []
        self.__requisito = requisito

    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def requisito(self):
        return self.__requisito

    @requisito.setter
    def requisito(self, requisito):
        self.__nome = requisito

    '''
    def add_funcionario(self, funcionario: Funcionario):
        if (funcionario is not None) and (isinstance(funcionario, Funcionario)):
            if funcionario not in self.__funcionarios:
                self.__funcionarios.append(funcionario)
                #for a in self.__funcionarios:
                    #print(a.nome)
            if self not in funcionario.servicos:
                funcionario.servicos.append(self)
                #for i in funcionario.servicos:
                    #print(i.nome)
    '''

    kit_unha = Ferramenta("Kit unha")
    kit_cabelo = Ferramenta("Kit cabelo")
    kit_pele = Ferramenta("Kit pele")