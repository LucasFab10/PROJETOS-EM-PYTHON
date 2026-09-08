import datetime


class Poupanca:
    
    def __init__(self, taxa_remuneracao):
        self.taxaremuneracaoMes = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneraConta(self): # Aplica a remuneração a conta
        self.saldo += self.saldo * self.taxaremuneracaoMes