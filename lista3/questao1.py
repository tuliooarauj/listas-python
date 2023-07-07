qtd_criaturas = int(input())

lista_criaturas = []
for i in range(qtd_criaturas):
    criatura = input()
    lista_criaturas.append(criatura)
    qtd_repetidos = lista_criaturas.count(criatura)
    if qtd_repetidos > 1:
        for x in range(1, qtd_repetidos):
            lista_criaturas.pop(-1)
            print('Criatura repetida')


print('Registradas:')
for criaturas in lista_criaturas:
    print(criaturas)
