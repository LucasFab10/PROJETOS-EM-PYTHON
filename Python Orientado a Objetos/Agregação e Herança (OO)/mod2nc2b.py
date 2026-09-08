from cliente import Cliente
from conta import Conta


cliente1 = Cliente(
    cpf="123",
    nome="Lucas",
    endereco="Rua X"
)

cliente2 = Cliente(
    cpf="456",
    nome="Gabriel",
    endereco="Rua W"
)


conta1 = Conta(
    clientes=[cliente1, cliente2],
    numero=1,
    saldo=2000
)


print("Saldo inicial:")
conta1.gerarsaldo()


conta1.depositar(1000)

print("\nApós depósito de R$1000:")
conta1.gerarsaldo()


conta1.sacar(1500)

print("\nApós saque de R$1500:")
conta1.gerarsaldo()


print("\nExtrato:")
conta1.extrato.gerar_extrato(conta1.numero)