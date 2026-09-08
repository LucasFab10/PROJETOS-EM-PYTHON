#construtores e métodos init e self
#self é a forma da classe se referir a ela mesma
# __init__ é o método construtor que cria o objeto da classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo