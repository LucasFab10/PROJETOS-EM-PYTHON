class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transferirValor(self, contaDestino, valor):
        # Tenta sacar o dinheiro da conta de origem
        if self.sacar(valor):
            # Se conseguiu sacar, deposita na conta destino
            contaDestino.depositar(valor)
            return True
        else:
            return False

    def gerar_extrato(self):
        print(f"Número: {self.numero}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R${self.saldo}")


def main():
    conta1 = Conta(numero=1, cpf=123, nomeTitular="Joao", saldo=1000)
    conta2 = Conta(numero=3, cpf=456, nomeTitular="Lucas", saldo=1000)

    if conta1 != conta2:
        print("As contas são objetos diferentes.")

        print("\nSaldo antes da transferência:")
        print(f"Saldo da conta1: R${conta1.saldo}")
        print(f"Saldo da conta2: R${conta2.saldo}")

        valor = 857

        if conta1.transferirValor(conta2, valor):
            print("\nTransferência realizada com sucesso!")

            print("\nSaldo após a transferência:")
            print(f"Saldo da conta1: R${conta1.saldo}")
            print(f"Saldo da conta2: R${conta2.saldo}")

        else:
            print("\nSaldo insuficiente para realizar a transferência.")

    else:
        print("As contas são o mesmo objeto.")


if __name__ == "__main__":
    main()