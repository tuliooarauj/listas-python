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

mesma_posicao = False
pipoca_encontrada = False
pipoca_destruida = False

while (voceY == barbieY and voceX == barbieX) or (voceY == oppenheimerY and voceX == oppenheimerX) or (mesma_posicao): 

    if not mesma_posicao: #personagem encontrado pelo cambista
        if not pipoca_encontrada:
            print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
        else:
            if voceX == barbieX and voceY == barbieY:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
            elif voceX == oppenheimerX and voceY == oppenheimerY:
                print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
    else:
        print('Droga! Agora volto pra casa sem filme e sem dinheiro.')


else:
    sentido_deslocado = input()


    dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2)**1/2
    cambista_perto = 'Preciso acelerar, o cambista tá na minha cola!\n'
    cambista_medio = 'Consigo ver lá longe o cambista, mas é melhor acelerar!\n'
    cambista_longe = 'O cambista está longe, mas não posso ficar parado\n'

    if pipoca_encontrada:
        print('Finalmente! Peguei a pipoca')

    if cambistaY > voceY: #cambista está a direita do personagem
        matriz_valores[cambistaX][cambistaY] = '- '
        cambistaY -= 1
        matriz_valores[cambistaX][cambistaY] = 'C'
        if cambistaX == pipocaX and cambistaY == pipocaY:
            pipoca_destruida = True
    elif cambistaY < voceY: #cambista está a esquerda do personagem
        matriz_valores[cambistaX][cambistaY] = '- '
        cambistaY += 1
        matriz_valores[cambistaX][cambistaY] = 'C'
        if cambistaX == pipocaX and cambistaY == pipocaY:
            pipoca_destruida = True
    else:
        #cambista na mesma coluna do personagem

        if cambistaX > voceX: #cambista está abaixo do personagem
            matriz_valores[cambistaX][cambistaY] = '- '
            cambistaX -= 1
            matriz_valores[cambistaX][cambistaY] = 'C'
            if cambistaX == pipocaX and cambistaY == pipocaY:
                pipoca_destruida = True
        elif cambistaX < voceX: #cambista está acima do personagem
            matriz_valores[cambistaX][cambistaY] = '- '
            cambistaX += 1
            matriz_valores[cambistaX][cambistaY] = 'C'
            if cambistaX == pipocaX and cambistaY == pipocaY:
                pipoca_destruida = True
        else:
            mesma_posicao = True

    if sentido_deslocado == 'esquerda':
        matriz_valores[voceX][voceY] = '- '
        voceY -= 1
        matriz_valores[voceX][voceY] = 'V'
        if not pipoca_destruida:
            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
            else:
                if not pipoca_encontrada:
                    print('Ainda não achei a pipoca')
        if dVC <= 3:
            print(cambista_perto)
        elif dVC > 3 and dVC <= 4:
            print(cambista_medio)
        elif dVC > 4:
            print(cambista_longe)

    if sentido_deslocado == 'direita':
        matriz_valores[voceX][voceY] = '- '
        voceY += 1
        matriz_valores[voceX][voceY] = 'V'
        if not pipoca_destruida:
            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
            else:
                if not pipoca_encontrada:
                    print('Ainda não achei a pipoca')
        if dVC <= 3:
            print(cambista_perto)
        elif dVC > 3 and dVC <= 4:
            print(cambista_medio)
        elif dVC > 4:
            print(cambista_longe)

    if sentido_deslocado == 'cima':
        matriz_valores[voceX][voceY] = '- '
        voceX -= 1
        matriz_valores[voceX][voceY] = 'V'
        if not pipoca_destruida:
            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
            else:
                if not pipoca_encontrada:
                    print('Ainda não achei a pipoca')
        if dVC <= 3:
            print(cambista_perto)
        elif dVC > 3 and dVC <= 4:
            print(cambista_medio)
        elif dVC > 4:
            print(cambista_longe)
    
    if sentido_deslocado == 'baixo':
        matriz_valores[voceX][voceY] = '- '
        voceX += 1
        matriz_valores[voceX][voceY] = 'V'
        if not pipoca_destruida:
            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
            else:
                if not pipoca_encontrada:
                    print('Ainda não achei a pipoca')
        if dVC <= 3:
            print(cambista_perto)
        elif dVC > 3 and dVC <= 4:
            print(cambista_medio)
        elif dVC > 4:
            print(cambista_longe)

    for linhas in matriz_valores:
        print(linhas)



print()
