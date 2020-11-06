import datetime

class TelaAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controle = controlador_atendimento

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico inteiro válido")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def tela_opcoes(self):
        print(" ---- Cadastro de Atendimentos ---- ")
        print("Escolha a opção")
        print("1: Marcar Atendimento")
        print("2: Excluir Atendimento")
        print("3: Alterar Atendimento")
        print("4: Listar Atendimentos por Cliente")
        print("5: Listar Atendimentos por Dia")
        print("6: Relatório do mês - número de atendimentos por serviço")
        print("0: Retorna")

        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 6, 0])
        return opcao

    def solicita_dados_atendimento(self):
        print(" ---- Marcar Atendimento ---- ")
        servico = input("Serviço a ser marcado: ")
        cliente = input("Nome do cliente: ")
        funcionario = input("Nome do funcionário: ")
        try:
            data = input("Data do atendimento (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            if ano < datetime.date.today().year:
                raise ValueError
            data_atendimento = datetime.date(ano, mes, dia)
        except ValueError:
            print ("Data inválida!")
            self.__controle.inclui_atendimento()
        try:
            hora = input("Hora do atendimento (HH:MM): ")
            h, m = map(int, hora.split(':'))
            hora_atendimento = datetime.time(h, m)
        except ValueError:
            print("Horário inválido!")
            self.__controle.inclui_atendimento()
        valor = input("Valor do atendimento: R$")
        try:
            valor = float(valor)
        except ValueError:
            print("Valor float inválido")
        pago = input("Pago agora (True/False):")
        try:
            pago = bool(pago)
        except ValueError:
            print("Valor booleano inválido")
            self.__controle.inclui_atendimento()
        dados_atendimento = {"servico": servico, "cliente": cliente, "funcionario": funcionario,
                                 "data": data_atendimento, "hora": hora_atendimento, "valor": valor, "pago": pago}
        return dados_atendimento

    def encontra_atendimento(self):
        print(" ---- Exclusão de Atendimento ---- ")
        id = int(input("Insira o ID do atendimento para excluir: "))
        return id

    def altera_dados_atendimento(self):
        print(" --- Alteração de Atendimento ---")
        id = input("Insira o ID do atendimento: ")
        try:
            id = int(id)
        except ValueError:
            print("Tipo de valor inválido!")
            self.__controle.altera_atendimento()
        print("Dados: servico, cliente, funcionario, data, hora, valor, pago")
        try:
            dado = input("Dado a ser alterado: ")
            if dado != "servico" or dado != "cliente" or dado != "funcionario" or dado != "data" or dado != "hora" or \
               dado != "valor" or dado != "pago":
                raise ValueError
        except ValueError:
            print("Dado inválido! Dados: servico, cliente, funcionario, data, hora, valor, pago")
            self.__controle.altera_atendimento()
        if dado == "data":
            try:
                data = input("Insira a " + dado +" (DIA/MÊS/ANO): ")
                dia, mes, ano = map(int, data.split('/'))
                valor = datetime.date(ano, mes, dia)
            except ValueError:
                print("Data inválida!")
                self.__controle.altera_atendimento()
        elif dado == "hora":
            try:
                hora = input("Insira a "+ dado +"(HH:MM): ")
                h, m = map(int, hora.split(':'))
                valor = datetime.time(h, m)
            except ValueError:
                print("Horário inválido!")
                self.__controle.altera_atendimento()
        elif dado == "pago":
            valor = input("Insira o "+dado+"(True/False): ")
            try:
                valor = bool(valor)
            except ValueError:
                print("Valor booleano inválido!")
                self.__controle.altera_atendimento()
        elif dado == "valor":
            valor = input("Insira o "+dado+": ")
            try:
                valor = float(valor)
            except ValueError:
                print("Valor float inválido!")
                self.__controle.altera_atendimento()
        else:
            valor = input("Insira o " + dado + ": ")
        return id, dado, valor

    def atendimento_cliente(self):
        print(" --- Atendimentos por Cliente --- ")
        cliente = input("Insira o nome do cliente: ")
        return cliente

    def atendimento_dia(self):
        print(" --- Atendimentos por Dia --- ")
        try:
            data = input("Insira a data (DIA/MES/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            data_atendimento = datetime.date(ano, mes, dia)
        except ValueError:
            print("Data inválida!")
        return data_atendimento

    def mostra_dados_atendimento(self, id: int, servico, cliente, funcionario, data, hora, valor, pago):
        print("ID: ", id)
        print("Servico: ", servico.nome)
        print("Cliente: ", cliente.nome)
        print("Funcionario: ", funcionario.nome)
        print("Data e hora: "+data+ ", ", hora)
        print("Valor: R$", valor)
        print("Pago: ", pago)

    def relatorio_mes(self):
        print(" --- Relatório do Mês --- ")
        mes = input("Insira o mês (1-12): ")
        try:
            mes = int(mes)
            if mes > 12 or mes < 1:
                raise ValueError
        except ValueError:
            print("Mês inválido!")
        return mes

    def mostra_relatorio(self):
        pass

    def excecao(self, mensagem):
        print(mensagem)