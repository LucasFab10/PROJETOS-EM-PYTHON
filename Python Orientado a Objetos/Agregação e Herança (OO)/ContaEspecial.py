from Conta.conta import Conta


class ContaEspecial(Conta):

    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return False

        if valor > self.saldo + self.limite:
            print("Limite insuficiente.")
            return False

        self.saldo -= valor

        print(f"Saque de R$ {valor:.2f} realizado.")

        return True

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return False

        self.saldo += valor

        print(f"Depósito de R$ {valor:.2f} realizado.")

        return True