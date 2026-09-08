def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('Acabou!')
regressiva(10)

#Não recursiva
for y in range(10 ,-1, -1):
    print(y)
print('Acabou')     