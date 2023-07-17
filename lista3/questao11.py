voceX = int(input()) 
voceY = int(input())

cambistaX = int(input())
cambistaY = int(input())

pipocaX = int(input())
pipocaY = int(input())

barbieX = int(input())
barbieY = int(input())

oppenheimerX = int(input())
oppenheimerY = int(input())

matriz_valores = []

for linha in range(8):
    lista_matriz = []
    for coluna in range(8):
        lista_matriz.append('- ')
    matriz_valores.append(lista_matriz)

    if linha == voceX:
        for valor_coluna in matriz_valores:
            matriz_valores[linha][voceY] = 'V'


    if linha == cambistaX:
        for valor_coluna in matriz_valores:
            matriz_valores[linha][cambistaY] = 'C'


    if linha == pipocaX:
        for valor_coluna in matriz_valores:
            matriz_valores[linha][pipocaY] = 'P'


    if linha == barbieX:
        for valor_coluna in matriz_valores:
            matriz_valores[linha][barbieY] = 'B'


    
    if linha == oppenheimerX:
        for valor_coluna in matriz_valores:
            matriz_valores[linha][oppenheimerY] = 'O'



    print(lista_matriz)

while (voceY != barbieY and voceX != barbieX) or (voceY != oppenheimerY and voceX != oppenheimerX): 
    sentido_deslocado = input()
    
    if sentido_deslocado == 'esquerda':
        matriz_valores[voceX][voceY] = '- '
        voceY -= 1
        matriz_valores[voceX][voceY] = 'V'
    if sentido_deslocado == 'direita':
        voceY +- 1

    for linhas in matriz_valores:
        print(linhas)


print()
