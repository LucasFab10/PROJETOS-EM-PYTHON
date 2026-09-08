# Testando Herança

from Cliente.cliente import Cliente
from Conta.conta import Conta
from ContaEspecial import ContaEspecial


cliente1 = Cliente(
    cpf="123",
    nome="Maria",
    endereco="Rua J"
)

cliente2 = Cliente(
    cpf="456",
    nome="João",
    endereco="Rua X"
)

cliente3 = Cliente(
    cpf="789",
    nome="Joana",
    endereco="Rua H"
)


conta1 = Conta(
    clientes=[cliente1],
    numero=1,
    saldo=2000
)

conta2 = Conta(
    clientes=[cliente2],
    numero=2,
    saldo=2000
)

conta3 = ContaEspecial(
    clientes=[cliente3],
    numero=3,
    saldo=1000,
    limite=2000
)


print(
    f"Cliente: {cliente1.cpf} | "
    f"Conta comum: {conta1.numero} | "
    f"Saldo: R$ {conta1.saldo:.2f}"
)

print(
    f"Cliente: {cliente2.cpf} | "
    f"Conta comum: {conta2.numero} | "
    f"Saldo: R$ {conta2.saldo:.2f}"
)

print(
    f"Cliente: {cliente3.cpf} | "
    f"Conta especial: {conta3.numero} | "
    f"Saldo: R$ {conta3.saldo:.2f} | "
    f"Limite: R$ {conta3.limite:.2f}"
)


print("\n--- Conta comum ---")

conta2.depositar(500)

print(
    f"Saldo após depósito: "
    f"R$ {conta2.saldo:.2f}"
)

conta2.sacar(3000)

print(
    f"Saldo após tentativa de saque: "
    f"R$ {conta2.saldo:.2f}"
)


print("\n--- Conta especial ---")

conta3.depositar(100)

print(
    f"Saldo após depósito: "
    f"R$ {conta3.saldo:.2f}"
)

conta3.sacar(2000)

print(
    f"Saldo após saque: "
    f"R$ {conta3.saldo:.2f}"
)

print(
    f"Limite restante: "
    f"R$ {conta3.limite:.2f}"
)


print("\nTentativa de ultrapassar o limite:")

conta3.sacar(2000)

print(
    f"Saldo final: "
    f"R$ {conta3.saldo:.2f}"
)

print(
    f"Limite final: "
    f"R$ {conta3.limite:.2f}"
)