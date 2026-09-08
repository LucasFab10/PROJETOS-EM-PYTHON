vnr = eval(input('Digite um número:'))
print('Número digitado:', vnr)
print('Antes do if')

if vnr <= 100: 
    print('Entrou no if')
elif vnr <= 500:
    print('Entrou no elif do 500')

else: 
    print('Entrou no else')
    