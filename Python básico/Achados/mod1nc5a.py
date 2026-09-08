
for num in range (32, 99):
    menor = num % 100 # Obtém o número do algarismo menos significativo
    maior = num // 100 # Obtém o número do algarismo mais significativo
    raiz = menor + maior # Obtém a raiz

    if (raiz * raiz) == num: # Valida se a raiz gera o número testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('Terminou')
print('Saiu', num)