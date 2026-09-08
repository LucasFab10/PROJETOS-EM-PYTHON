from datetime import datetime
from Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return False

        self.saldo += valor

        self.extrato.transacoes.append(
            ["DEPÓSITO", valor, datetime.today()]
        )

        return True

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return False

        if self.saldo < valor:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor

        self.extrato.transacoes.append(
            ["SAQUE", valor, datetime.today()]
        )

        return True

    def transfereValor(self, contaDestino, valor):
        if valor <= 0:
            return "O valor da transferência deve ser positivo."

        if self.saldo < valor:
            return "Não existe saldo suficiente."

        contaDestino.depositar(valor)
        self.saldo -= valor

        self.extrato.transacoes.append(
            ["TRANSFERÊNCIA", valor, datetime.today()]
        )

        return "Transferência realizada."

    def gerarsaldo(self):
        print(f"Número: {self.numero} | Saldo: R$ {self.saldo:.2f}")