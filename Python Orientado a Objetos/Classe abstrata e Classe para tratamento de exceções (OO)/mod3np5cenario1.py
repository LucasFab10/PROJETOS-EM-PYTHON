# Criar um sistema de classes para modelar diferentes
# tipos de veículos,
# utilizando uma classe abstrata como base para definir 
# a interface comum.
# Chame os métodos mover() e ligar() em cada instância.

from abc import ABC, abstractmethod

# Classe abstrata veículo

class Veiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def ligar(self):
        pass

# Subclasse carro
class Carro(Veiculo):

    def mover(self):
        return "O carro está se movendo."

    def ligar(self):
        return "O carro está ligando."

# Subclasse bicicleta
class Bicicleta(Veiculo):

    def mover(self):
        return "A bicicleta está se movendo."

    def ligar(self):
        return "Não é possível ligar uma bicicleta"

# Testando as implementações
carro = Carro()
bicicleta = Bicicleta()

print(carro.mover()) # Saída: O carro está se movendo.
print(carro.ligar()) # Saída: O carro está ligando.

print(bicicleta.mover()) # Saída: A bicicleta está se movendo.
print(bicicleta.ligar()) # Saída: Não é possível ligar uma bicicleta
