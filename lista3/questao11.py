voceY = int(input())
voceX = int(input())

cambistaY = int(input())
cambistaX = int(input())

pipocaY = int(input())
pipocaX = int(input())

barbieY = int(input())
barbieX = int(input())

oppenheimerY = int(input())
oppenheimerX = int(input())

for linha in range(7):
    lista_matriz = []
    for coluna in range(7):
        if linha == 0 and coluna == 0:
            lista_matriz.append('- ')
        if linha == voceX:
            lista_matriz.insert([voceY], 'V')

        if lista_matriz[coluna] != 'V' and lista_matriz[coluna] != 'C' and lista_matriz[coluna] != 'P' and lista_matriz[coluna] != 'B' and lista_matriz[coluna] != 'O':

            lista_matriz.append('- ')


        matriz = ''.join(lista_matriz)
    print(matriz)

print(lista_matriz[3][5])



