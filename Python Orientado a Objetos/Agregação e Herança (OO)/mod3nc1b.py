from Cliente.cliente import Cliente
from Conta.conta import Conta
from Poupanca.poupanca import Poupanca
from ContaRemuneradaPoupanca.contaremuneradapoupanca import ContaRemuneradaPoupanca


cliente1 = Cliente(cpf= "123", nome= "João", endereco= "Rua X")
cliente2 = Cliente(cpf= "456", nome= "Maria", endereco= "Rua W")

conta1 = Conta(clientes= [cliente1, cliente2], numero= 1, saldo= 2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(taxa_remuneracao=0.1, clientes=[cliente1], numero=5, saldo=1000)

contaremunerada1.remuneraConta()
contaremunerada1.gerarsaldo()