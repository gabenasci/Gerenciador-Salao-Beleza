from entidade.funcionario import Funcionario

class Servico:
    def __init__(self, nome: str, contra_indicacao: bool):
        self.__nome = nome
        self.__funcionarios = []
        self.__contra_inicacao: contra_indicacao
        if contra_indicacao == True:
            self.__qual_contra_indic: ""

    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome (self, nome):
        self.__nome = nome

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def contra_indicacao(self):
        return self.contra_indicacao

    @contra_indicacao.setter
    def contra_indicacao(self, contra_indicacao):
        if isinstance(contra_indicacao, bool):
            self.contra_indicacao = contra_indicacao

    @property
    def qual_contra_indic(self):
        return self.__qual_contra_indic

    @qual_contra_indic.setter
    def qual_contra_indic(self, qual_contra_indic):
        if isinstance(qual_contra_indic, str):
            self.__qual_contra_indic = qual_contra_indic

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