# Herança múltipla

from Conta.conta import Conta
from Poupanca.poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):

    def __init__(self, taxa_remuneracao, clientes, numero, saldo):

        # Inicializa os atributos herdados da classe Conta
        Conta.__init__(self, clientes, numero, saldo)

        # Inicializa os atributos herdados da classe Poupanca
        Poupanca.__init__(self, taxa_remuneracao)

    def remuneraConta(self):
        # Aplica a remuneração à conta
        self.saldo += self.saldo * (self.taxaremuneracaoMes / 30)