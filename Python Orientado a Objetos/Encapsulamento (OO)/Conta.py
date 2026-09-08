class Conta: 
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
            if valor > 0:
                self.__saldo += valor
                print(f"Depósito de R$ {valor:.2f} realizado.")
            else:
                print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
            if valor <= 0:
                print("O valor do saque deve ser positivo.")
            elif valor > self.__saldo:
                print("Saldo insuficiente.")
            else:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado.")

    def consultar_saldo(self):
            return self.__saldo


conta = Conta("Lucas", 1000)

print(f"Titular: {conta.titular}")
print(f"Saldo: R${conta.consultar_saldo():.2f}")

conta.depositar(500)
conta.sacar(200)

print(f"Saldo atual: R${conta.consultar_saldo():.2f}")
    