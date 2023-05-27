
# > DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome':'Ana', 'idade':37, 'altura':1.60 }

print(dicionario)
print(dicionario['idade'])


# Adicionando elementos em um dicionário


dicionario['Programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Interando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)


