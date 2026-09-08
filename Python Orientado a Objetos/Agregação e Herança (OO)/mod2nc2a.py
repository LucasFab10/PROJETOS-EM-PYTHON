from cliente import Cliente
from conta import Conta


cliente1 = Cliente(cpf=123, nome="Lucas", endereco="Rua 1")
cliente2 = Cliente(cpf=345, nome="Gabriel", endereco="Rua 2")


conta1 = Conta(
    clientes=[cliente1, cliente2],
    numero=1,
    saldo=0
)


conta1.gerarsaldo()

conta1.depositar(1500)

conta1.sacar(500)

conta1.gerarsaldo()