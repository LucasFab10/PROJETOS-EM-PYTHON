# Classe abstrata e método abstrato
# Classe que não pode ser instânciada
from abc import ABC, abstractmethod
#abc (Abstract Base Classes). Super classes de uma classe abstrata
class ContaCliente(ABC):
    def __init__ (self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

        #decorator @abstractmethod para indicar que o método calculo_rendimento 

        @abstractmethod
        def CalculoRendimento(self):
            pass

class ContaReal(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    def CalculoRendimento(self):
        pass

cc1 = ContaCliente(numero=1,IOF= 0.1,IR= 0.25,valorinvestido= 10.1, taxarendimento= 10)
print(cc1)
print(cc1.numero)
print(cc1.valorinvestido)