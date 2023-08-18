dados_pessoais = {'nome': 'Tulio', 'idade': '19', 'curso': 'Ciência da Computação'}
print(dados_pessoais)
#As access keys podem ser integers tb, porém seus acessos serão pelo indíce em colchete. Ex: [1]

champions = {1: 'Tulio', 2: 'Eduarda', 'medalha': 'Ouro, Prata'}
print(champions[1])
print(champions.get(2))
print(dados_pessoais.get('idade', 'Inexistente')) #procura chave idade, se não tiver, retorna inexistente

#Atualizando dicionário ao adicionar uma key até então inexistente
dados_pessoais.update({'telefone': '93222-1233' })
print(dados_pessoais)

#Atualizando dados
dados_pessoais['idade'] = 20
print(dados_pessoais)

#Atualizando dicionário ao dar update em todas as keys 
dados_pessoais.update({'nome': 'Eduarda', 'idade': '18', 'curso': 'Medicina'})
print(dados_pessoais)

#Removendo dados com del
del dados_pessoais['telefone']
print(dados_pessoais)

#Removendo dados com pop
medalhas = champions.pop('medalha')
print(champions)
print(medalhas)

#Comandos importantes para dicionários
#len -- > tamanho dicionario
# keys() --> retorna as chaves
# values() --> retorna os valores associados a cada chave
# items() --> retorna os pares(chave, valor)

print(len(dados_pessoais))
print(dados_pessoais.keys())
print(dados_pessoais.values())
print(dados_pessoais.items())

for chave in dados_pessoais:
    print(chave)
for chave, valor in dados_pessoais.items():
    print(chave, valor)


