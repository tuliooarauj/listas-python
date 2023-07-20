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
        lista_matriz.append('-')
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

mesma_posicao = False
pipoca_encontrada = False
pipoca_destruida = False

cambista_perto = 'Preciso acelerar, o cambista tá na minha cola!\n'
cambista_medio = 'Consigo ver lá longe o cambista, mas é melhor acelerar!\n'
cambista_longe = 'O cambista está longe, mas não posso ficar parado\n'

cont = 0


while not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX) and (mesma_posicao == False): 

    cont += 1

    sentido_deslocado = input()

    if cambistaY > voceY: #cambista está a direita do personagem
        matriz_valores[cambistaX][cambistaY] = '-'
        cambistaY -= 1
        matriz_valores[cambistaX][cambistaY] = 'C'
        if cambistaX == pipocaX and cambistaY == pipocaY:
            pipoca_destruida = True
        elif cambistaX == voceX and cambistaY == voceY:
            mesma_posicao = True
    elif cambistaY < voceY: #cambista está a esquerda do personagem
        matriz_valores[cambistaX][cambistaY] = '-'
        cambistaY += 1
        matriz_valores[cambistaX][cambistaY] = 'C'
        if cambistaX == pipocaX and cambistaY == pipocaY:
            pipoca_destruida = True
        elif cambistaX == voceX and cambistaY == voceY:
            mesma_posicao = True
    else:
        #cambista na mesma coluna do personagem

        if cambistaX > voceX: #cambista está abaixo do personagem
            matriz_valores[cambistaX][cambistaY] = '-'
            cambistaX -= 1
            matriz_valores[cambistaX][cambistaY] = 'C'
            if cambistaX == pipocaX and cambistaY == pipocaY:
                pipoca_destruida = True
            elif cambistaX == voceX and cambistaY == voceY:
                mesma_posicao = True
        elif cambistaX < voceX: #cambista está acima do personagem
            matriz_valores[cambistaX][cambistaY] = '-'
            cambistaX += 1
            matriz_valores[cambistaX][cambistaY] = 'C'
            if cambistaX == pipocaX and cambistaY == pipocaY:
                pipoca_destruida = True
            elif cambistaX == voceX and cambistaY == voceY:
                mesma_posicao = True
        
    if not mesma_posicao:
#===========================================================================================================
#                   ESQUERDA
#===========================================================================================================

        if pipoca_encontrada == False and sentido_deslocado == 'esquerda':
            matriz_valores[voceX][voceY] = '-'
            voceY -= 1
            matriz_valores[voceX][voceY] = 'V'
            if voceX == cambistaX and voceY == cambistaY:
                mesma_posicao = True
                matriz_valores[voceX][voceY] = 'C'
            for linhas in matriz_valores:
                    print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                    
            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
                rodada_pipoca_encontrada = cont
            else:
                if not pipoca_encontrada:
                    if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                        print('Ainda não achei a pipoca')

            dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
            if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                if dVC <= 3:
                    print(cambista_perto)
                elif dVC > 3 and dVC <= 4:
                    print(cambista_medio)
                elif dVC > 4:
                    print(cambista_longe)

        else:
            #Pipoca foi destruída ou ja encontrada
            if sentido_deslocado == 'esquerda':
                if pipoca_destruida:
                    matriz_valores[voceX][voceY] = '-'
                    voceY -= 1
                    matriz_valores[voceX][voceY] = 'V'
                    if voceX == cambistaX and voceY == cambistaY:
                        mesma_posicao = True
                        matriz_valores[voceX][voceY] = 'C'
                    for linhas in matriz_valores:
                        print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)


                if pipoca_encontrada:
                    if cont >= rodada_pipoca_encontrada + 2:
                        matriz_valores[voceX][voceY] = '-'
                        voceY -= 1
                        matriz_valores[voceX][voceY] = 'V'
                        if voceX == cambistaX and voceY == cambistaY:
                            mesma_posicao = True
                            matriz_valores[voceX][voceY] = 'C'
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                        if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                            print('Já peguei a pipoca')
                    else:
                        #ainda está parado na rodada
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                        print('Já peguei a pipoca')

                if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                    dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                    if dVC <= 3:
                        print(cambista_perto)
                    elif dVC > 3 and dVC <= 4:
                        print(cambista_medio)
                    elif dVC > 4:
                        print(cambista_longe)

    #===========================================================================================================
    #                   DIREITA
    #===========================================================================================================


        if pipoca_encontrada == False and sentido_deslocado == 'direita':
            matriz_valores[voceX][voceY] = '-'
            voceY += 1
            matriz_valores[voceX][voceY] = 'V'
            if voceX == cambistaX and voceY == cambistaY:
                mesma_posicao = True
                matriz_valores[voceX][voceY] = 'C'
            for linhas in matriz_valores:
                    print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                pipoca_encontrada = True
                rodada_pipoca_encontrada = cont
            else:
                if not pipoca_encontrada:
                    if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                        print('Ainda não achei a pipoca')

            dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
            if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                if dVC <= 3:
                    print(cambista_perto)
                elif dVC > 3 and dVC <= 4:
                    print(cambista_medio)
                elif dVC > 4:
                    print(cambista_longe)

        else:
            #Pipoca foi destruída ou ja encontrada
            if sentido_deslocado == 'direita':

                if pipoca_destruida:
                    matriz_valores[voceX][voceY] = '-'
                    voceY += 1
                    matriz_valores[voceX][voceY] = 'V'
                    if voceX == cambistaX and voceY == cambistaY:
                        mesma_posicao = True
                        matriz_valores[voceX][voceY] = 'C'
                    for linhas in matriz_valores:
                        print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

                if pipoca_encontrada:

                    if cont >= rodada_pipoca_encontrada + 2:
                        matriz_valores[voceX][voceY] = '-'
                        voceY += 1
                        matriz_valores[voceX][voceY] = 'V'
                        if voceX == cambistaX and voceY == cambistaY:
                            mesma_posicao = True
                            matriz_valores[voceX][voceY] = 'C'
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                        if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                            print('Já peguei a pipoca')

                    else:
                        #ainda está parado na rodada
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                        print('Já peguei a pipoca')
                    
                if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                    dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                    if dVC <= 3:
                        print(cambista_perto)
                    elif dVC > 3 and dVC <= 4:
                        print(cambista_medio)
                    elif dVC > 4:
                        print(cambista_longe)

    #===========================================================================================================
    #                   CIMA
    #===========================================================================================================


        if pipoca_encontrada == False and sentido_deslocado == 'cima':
            matriz_valores[voceX][voceY] = '-'
            voceX -= 1
            matriz_valores[voceX][voceY] = 'V'
            if voceX == cambistaX and voceY == cambistaY:
                mesma_posicao = True
                matriz_valores[voceX][voceY] = 'C'
            for linhas in matriz_valores:
                    print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

            if voceX == pipocaX and voceY == pipocaY:
                print('Finalmente! Peguei a pipoca')
                rodada_pipoca_encontrada = cont
                pipoca_encontrada = True
            else:
                if not pipoca_encontrada:
                    if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                        print('Ainda não achei a pipoca')

            if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                if dVC <= 3:
                    print(cambista_perto)
                elif dVC > 3 and dVC <= 4:
                    print(cambista_medio)
                elif dVC > 4:
                    print(cambista_longe)
        else:
            #Pipoca foi destruída ou ja encontrada
            if sentido_deslocado == 'cima':

                if pipoca_destruida:
                    matriz_valores[voceX][voceY] = '-'
                    voceX -= 1
                    matriz_valores[voceX][voceY] = 'V' 
                    if voceX == cambistaX and voceY == cambistaY:
                        mesma_posicao = True
                        matriz_valores[voceX][voceY] = 'C'
                    for linhas in matriz_valores:
                        print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

                if pipoca_encontrada:
                    if cont >= rodada_pipoca_encontrada + 2:
                        matriz_valores[voceX][voceY] = '-'
                        voceX -= 1
                        matriz_valores[voceX][voceY] = 'V' 
                        if voceX == cambistaX and voceY == cambistaY:
                            mesma_posicao = True
                            matriz_valores[voceX][voceY] = 'C'
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

                        if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                            print('Já peguei a pipoca')

                    else:
                        #ainda está parado na rodada
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)                
                        print('Já peguei a pipoca')

                if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                    dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                    if dVC <= 3:
                        print(cambista_perto)
                    elif dVC > 3 and dVC <= 4:
                        print(cambista_medio)
                    elif dVC > 4:
                        print(cambista_longe)


    #===========================================================================================================
    #                   BAIXO
    #===========================================================================================================

        
        if pipoca_encontrada == False and sentido_deslocado == 'baixo':
            matriz_valores[voceX][voceY] = '-'
            voceX += 1
            matriz_valores[voceX][voceY] = 'V'
            if voceX == cambistaX and voceY == cambistaY:
                mesma_posicao = True
                matriz_valores[voceX][voceY] = 'C'
            if not mesma_posicao:
                    for linhas in matriz_valores:
                        print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                    if voceX == pipocaX and voceY == pipocaY:
                        print('Finalmente! Peguei a pipoca')
                        pipoca_encontrada = True
                        rodada_pipoca_encontrada = cont
                    else:
                        if not pipoca_encontrada and not mesma_posicao:
                            if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                                print('Ainda não achei a pipoca')

                    if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX) and not mesma_posicao:
                        dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                        if dVC <= 3:
                            print(cambista_perto)
                        elif dVC > 3 and dVC <= 4:
                            print(cambista_medio)
                        elif dVC > 4:
                            print(cambista_longe)
        else:
            #Pipoca  foi destruída ou encontrada

            if sentido_deslocado == 'baixo':

                if pipoca_destruida:
                    matriz_valores[voceX][voceY] = '-'
                    voceX += 1
                    matriz_valores[voceX][voceY] = 'V'
                    if voceX == cambistaX and voceY == cambistaY:
                        mesma_posicao = True
                        matriz_valores[voceX][voceY] = 'C'
                    for linhas in matriz_valores:
                        print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

                if pipoca_encontrada:
                    if cont >= rodada_pipoca_encontrada + 2:
                        matriz_valores[voceX][voceY] = '-'
                        voceX += 1
                        matriz_valores[voceX][voceY] = 'V'
                        if voceX == cambistaX and voceY == cambistaY:
                            mesma_posicao = True
                            matriz_valores[voceX][voceY] = 'C'
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)

                        if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                            print('Já peguei a pipoca')
                    else:
                        #ainda está parado na rodada
                        for linhas in matriz_valores:
                            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
                        print('Já peguei a pipoca')
                
                if not mesma_posicao:

                  if not (voceY == barbieY and voceX == barbieX) and not (voceY == oppenheimerY and voceX == oppenheimerX):
                      dVC = ((voceX - cambistaX)**2 + (voceY - cambistaY)**2) ** 0.5
                      if dVC <= 3:
                          print(cambista_perto)
                      elif dVC > 3 and dVC <= 4:
                          print(cambista_medio)
                      elif dVC > 4:
                          print(cambista_longe)

    
else:
    if not mesma_posicao: #personagem nao encontrado pelo cambista
        if not pipoca_encontrada:
            print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
        else:
            if voceX == barbieX and voceY == barbieY:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
            elif voceX == oppenheimerX and voceY == oppenheimerY:
                print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
    else:
        for linhas in matriz_valores:
            print(' '.join(linhas)) #organizar essa ordem: (primeiro faz a conta, printa a matriz e so dps printa as mensagens)
        print('Droga! Agora volto pra casa sem filme e sem dinheiro.')