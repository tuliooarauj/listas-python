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
            valor_coluna.pop(voceY)      
            valor_coluna.insert(voceY, 'V')

    if linha == cambistaX:
        for valor_coluna in matriz_valores:
            valor_coluna.pop(cambistaY)      
            valor_coluna.insert(cambistaY, 'C')

    if linha == pipocaX:
        for valor_coluna in matriz_valores:
            valor_coluna.pop(pipocaY)      
            valor_coluna.insert(pipocaY, 'P')

    if linha == barbieX:
        for valor_coluna in matriz_valores:
            valor_coluna.pop(barbieY)      
            valor_coluna.insert(barbieY, 'B')
    
    if linha == oppenheimerX:
        for valor_coluna in matriz_valores:
            valor_coluna.pop(oppenheimerY)      
            valor_coluna.insert(oppenheimerY, 'O')

    print(lista_matriz)

while (voceY != barbieY and voceX != barbieX) or (voceY != oppenheimerY and voceX != oppenheimerX): 
    sentido_deslocado = input()
    

print()
