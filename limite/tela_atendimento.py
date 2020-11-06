import datetime

class TelaAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controle = controlador_atendimento

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

        opcao = int(input("Escolha a opção: "))
        return opcao

    def solicita_dados_atendimento(self):
        print(" ---- Marcar Atendimento ---- ")
        servico = input("Serviço a ser marcado: ")
        cliente = input("Nome do cliente: ")
        funcionario = input("Nome do funcionário: ")
        data = input("Data do atendimento (DIA/MES/ANO): ")
        dia, mes, ano = map(int, data.split('/'))
        data_atendimento = datetime.date(ano, mes, dia)
        hora = input("Hora do atendimento (HH:MM): ")
        h, m = map(int, hora.split(':'))
        hora_atendimento = datetime.time(h, m)
        valor = float(input("Valor do atendimento: R$"))
        pago = bool(input("Pago agora (True/False):"))
        dados_atendimento = {"servico": servico, "cliente": cliente, "funcionario": funcionario,
                             "data": data_atendimento, "hora": hora_atendimento, "valor": valor, "pago": pago}
        return dados_atendimento

    def encontra_atendimento(self):
        print(" ---- Exclusão de Atendimento ---- ")
        id = int(input("Insira o ID do atendimento para excluir: "))
        return id

    def altera_dados_atendimento(self):
        print(" --- Alteração de Atendimento ---")
        id = int(input("Insira o ID do atendimento: "))
        print("Dados: servico, cliente, funcionario, data, hora, valor, pago")
        dado = input("Dado a ser alterado: ")
        if dado == "data":
            data = input("Insira a " + dado +" (DIA/MÊS/ANO): ")
            dia, mes, ano = map(int, data.split('/'))
            valor = datetime.date(ano, mes, dia)
        elif dado == "hora":
            hora = input("Insira a "+ dado +"(HH:MM): ")
            h, m = map(int, hora.split(':'))
            valor = datetime.time(h, m)
        elif dado == "pago":
            valor = bool(input("Insira o "+dado+"(True/False): "))
        elif dado == "valor":
            valor = float(input("Insira o "+dado+": "))
        else:
            valor = input("Insira o " + dado + ": ")
        return id, dado, valor

    def atendimento_cliente(self):
        print(" --- Atendimentos por Cliente --- ")
        cliente = input("Insira o nome do cliente: ")
        return cliente

    def atendimento_dia(self):
        print(" --- Atendimentos por Dia --- ")
        data = input("Insira a data (DIA/MES/ANO): ")
        dia, mes, ano = map(int, data.split('/'))
        data_atendimento = datetime.date(ano, mes, dia)
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
        mes = int(input("Insira o mês (1-12): "))
        return mes

    def mostra_relatorio(self):
        pass

    def excecao(self, mensagem):
        print("Teste", mensagem)