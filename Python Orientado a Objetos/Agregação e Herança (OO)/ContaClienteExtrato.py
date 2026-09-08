import datetime
from Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo += valor

        self.extrato.transacoes.append(
            ["DEPÓSITO", valor, datetime.datetime.today()]
        )

        return True

    def sacar(self, valor):
        if valor <= 0:
            return False

        if self.saldo < valor:
            return False

        self.saldo -= valor

        self.extrato.transacoes.append(
            ["SAQUE", valor, datetime.datetime.today()]
        )

        return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente."

        contaDestino.depositar(valor)
        self.saldo -= valor

        self.extrato.transacoes.append(
            ["TRANSFERÊNCIA", valor, datetime.datetime.today()]
        )

        return "Transferência realizada."

    def gerarsaldo(self):
        print(f"Número: {self.numero} | Saldo: R$ {self.saldo:.2f}")