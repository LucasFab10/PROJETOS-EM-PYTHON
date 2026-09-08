#métodos de classes
# definem as ações que o objeto pode realizar
class Conta: 
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor): 
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")


def main():
    c1 = Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=0)
    c1.depositar(300) # Chamando o método depositar para c1
    c1.gerar_extrato() # Chamando o método para gerar o extrato para c1
    c1.sacar(100) # Chamando o método para sacar para c1
    c1.gerar_extrato() # Chamando o método para gerar o extrato para c1

if __name__ == "__main__":
    main()