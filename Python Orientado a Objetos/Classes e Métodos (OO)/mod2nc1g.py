#comunicação entre objetos na memória
# Uma classe pode ter várias instâncias (objetos) na memória,
# cada um com seus próprios valores de atributos.
# Para comparar se duas referências de memória apontam para o mesmo objeto,
# usamos os operadores == e !=

#métodos com retorno
# serve para validar o estado de um objeto

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor: # valida se existe saldo para o saque
            return False
        else: 
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}")

def main():
    conta1 = Conta(numero=1, cpf=123, nomeTitular='Joao', saldo=1000)
    conta2 = Conta(numero=3, cpf=456, nomeTitular='Lucas', saldo=1000)

    if (conta1 != conta2): # O "!" significa: não, ou seja: "!=" é = (Não igual)
        print("Endereços de memórias diferentes")

        print(conta1)
        print(conta2)

        print(conta1.saldo)
        print(conta2.saldo)
        conta1.depositar(300)
        print(conta1.saldo)
        print(conta2.saldo)

        conta1 = conta2
    else:
        print("Saldo insuficiente para realizar o saque.")

if __name__ == "__main__":
    main()

