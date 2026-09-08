dicionario = {
    "nome": "ALice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando e imprimindo valores individuais usando chaves
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cidade: {cidade}')

# Adicionando um novo par chave-valor ao dicionário
dicionario["Profissão"] = "Engenheira"
print(f'Dicionário após adicionar profissão: {dicionario}')

# Adicionando um novo par chave-valor ao dicionário
dicionario["idade"] = 26 # Atualizando o valor da chave "idade"
print(f'Dicionário após atualizar a idade: {dicionario}')

# Removendo um par chave-valor do dicionário
del dicionario["cidade"]
print(f'Dicionário após remover a cidade: {dicionario}')

# Acessando todas as chaves e valores do dicionário
chaves = dicionario.keys()
valores = dicionario.values()

print(f'Chaves; {list(chaves)}')
print(f'Valores: {list(valores)}')

# Iterando sobre os pares chave-valor do dicionário
print('Iterando sobre o dicionário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

    # Veificando se uma chave existe no dicionário
    if "nome" in dicionario:
        print(f'O nome dicionário é: {dicionario["nome"]}')

    else: 
        print('A chave "nome" não existe no dicionário.')

    # Usando o método get() para acessar valores de forma segura
    profissao = dicionario.get("Profissão", "Profissão não encontrada")
    print(f'Profissão: {profissao}')

    # Limpando todas os elementos do dicionário
    dicionario.clear()
    print(f'Dicionário após limpar todos os elementos: ')