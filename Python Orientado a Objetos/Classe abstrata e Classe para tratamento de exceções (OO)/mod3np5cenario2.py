# Cria uma classe chamada Calculadora que
# tenha métodos para
# realizar operações matemáticas básicas:
# adição, subtração, multiplicação e divisão.
#Implementação tratamento de exceções para 
# evitar tipos de dados incorretos

# Classe Calculadora com tratamento de exceções

class Calculadora:

    def adicao(self, x, y):
        try:
            return x + y
        except TypeError:
            return "Erro: Tipo de dados inválidos para adição."

    def subtracao(self, x, y):
        try:
            return x - y
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."

    def multiplicacao(self, x, y):
        try:
            return x * y
        except TypeError:
            return "Error: Tipo de dados inválidos para multiplicação."

    def divisao(self, x, y):
        try:
            return x / y
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."

# Testando as implementações
calculadora = Calculadora()

print(calculadora.adicao(x= 5, y= 3)) # Saída: 8
print(calculadora.subtracao(x= 5, y=3)) # Saída: 2
print(calculadora.multiplicacao(x= 5, y=3))# Saída: 15
print(calculadora.divisao(x=5, y= 'a')) # Saída: Erro: Tipos de dados inválido