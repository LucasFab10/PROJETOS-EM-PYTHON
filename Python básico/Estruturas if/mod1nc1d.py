vnr = eval(input('Digite um número:'))
print('Número digitado:', vnr)
print('Antes do if')
if vnr <= 100:
    print('Entrou no if do 100')
elif vnr <= 500:
    print('Entrou no elif do 500')
elif vnr <= 1000:
    print('Entrou no elif do 1000')
else: 
    print('Entrou no else')
print('Saiu do if')