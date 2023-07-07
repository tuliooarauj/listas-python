lista = [8, 3, 9, 1, 2, 3]
tamanho_lista = len(lista)
meio_lista = int(tamanho_lista/2)

lista1 = lista[:meio_lista]
lista2 = lista[meio_lista:]

lista_soma = []

for idx in range(meio_lista):
    lista_soma.append(lista1[idx] + lista2[idx])

print(lista)
print(lista1)
print(lista2)
print(lista_soma)

