
# SUPERCLASSE

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf  # dado sensível, por isso deixei "protegido" com _
        self.telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    def registrar_atendimento(self, tipo, custo):
        print(f"Paciente {self.nome} passou por um atendimento do tipo '{tipo}', "
              f"com custo de R$ {custo:.2f}.")

    def exibir_informacoes(self, detalhado=False):
        if not detalhado:
            print(f"Nome: {self.nome}")
            print(f"Prontuário: {self.numero_prontuario}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
        else:
            print(f"Nome: {self.nome}")
            print(f"Data de nascimento: {self.data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self.telefone}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Prontuário: {self.numero_prontuario}")



# SUBCLASSE 1 - PACIENTE PARTICULAR

class PacienteParticular(Paciente):
    """Paciente que paga direto pelo atendimento (sem convênio)."""

    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo,
                 numero_prontuario, forma_pagamento, desconto_fidelidade):
        # chama o __init__ da superclasse pra não repetir código
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def calcular_valor_final(self, valor_consulta, taxa_urgencia=0):
        valor_total = valor_consulta

        # se for atendimento de urgência, soma a taxa
        if taxa_urgencia > 0:
            valor_total += taxa_urgencia

        # aplica o desconto de fidelidade em cima do valor da consulta
        desconto = self.desconto_fidelidade * valor_consulta
        valor_total -= desconto

        return valor_total

    def exibir_informacoes(self, detalhado=False):
        # sobrescreve o método da superclasse, mas continua usando ele (polimorfismo)
        super().exibir_informacoes(detalhado)
        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Desconto de fidelidade: {self.desconto_fidelidade * 100:.0f}%")



# SUBCLASSE 2 - PACIENTE POR CONVÊNIO

class PacienteConvenio(Paciente):
    """Paciente atendido através de um plano de saúde."""

    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo,
                 numero_prontuario, nome_convenio, numero_carteirinha):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    def registrar_autorizacao(self, procedimento, valor_glosa=0):
        print(f"Procedimento autorizado pelo convênio: {procedimento}")
        print(f"Valor de glosa: R$ {valor_glosa:.2f}")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        print(f"Convênio: {self.nome_convenio}")
        print(f"Carteirinha: {self.numero_carteirinha}")



# TESTANDO O SISTEMA (área principal do programa)

if __name__ == "__main__":

    print("===== TESTANDO PACIENTE PARTICULAR =====")
    paciente1 = PacienteParticular(
        nome="Jose Willian",
        data_nascimento="14/03/1990",
        cpf="123.456.789-00",
        telefone="(21) 99999-1111",
        tipo_sanguineo="O+",
        numero_prontuario="P001",
        forma_pagamento="Pix",
        desconto_fidelidade=0.10
    )

    paciente1.exibir_informacoes(detalhado=False)
    print("-" * 40)
    paciente1.exibir_informacoes(detalhado=True)
    print("-" * 40)

    paciente1.registrar_atendimento("Consulta de rotina", 200.00)

    valor_final = paciente1.calcular_valor_final(valor_consulta=200.00, taxa_urgencia=50.00)
    print(f"Valor final a pagar: R$ {valor_final:.2f}")

    print("\n===== TESTANDO PACIENTE POR CONVÊNIO =====")
    paciente2 = PacienteConvenio(
        nome="karan Assad",
        data_nascimento="22/07/1985",
        cpf="987.654.321-00",
        telefone="(21) 98888-2222",
        tipo_sanguineo="A-",
        numero_prontuario="P002",
        nome_convenio="Unimed",
        numero_carteirinha="123456789"
    )

    paciente2.exibir_informacoes(detalhado=False)
    print("-" * 40)
    paciente2.exibir_informacoes(detalhado=True)
    print("-" * 40)

    paciente2.registrar_atendimento("Exame de sangue", 150.00)
    paciente2.registrar_autorizacao("Ressonância Magnética", valor_glosa=30.00)

