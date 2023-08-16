linha1 = input().split('|')
linha2 = input().split('|')
linha3 = input().split('|')

tabuleiro = [
    linha1[0],linha1[1],linha1[2],
    linha2[0],linha2[1],linha2[2],
    linha3[0],linha3[1],linha3[2]
]

jogador1 = 'x'
jogador2 = 'o'

def printa_tabuleiro(tabuleiro):
    print(tabuleiro[0] + '|' + tabuleiro[1] + '|' + tabuleiro[2])
    print(tabuleiro[3] + '|' + tabuleiro[4] + '|' + tabuleiro[5])
    print(tabuleiro[6] + '|' + tabuleiro[7] + '|' + tabuleiro[8])
    print('\n')
    
def verifica_espaco_disponivel(posicao):
    if posicao == '_':
        return True
    else:
        return False
    
def verifica_vitoria():
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[0] == tabuleiro[2] and tabuleiro[0] != '_': #Verificando linha 1
        return True
    elif tabuleiro[3] == tabuleiro[4] and tabuleiro[3] == tabuleiro[5] and tabuleiro[3] != '_': #Verificando linha 2
        return True
    elif  tabuleiro[6] == tabuleiro[7] and tabuleiro[6] == tabuleiro[8] and tabuleiro[6] != '_': #Verificando linha 3
        return True
    elif tabuleiro[0] == tabuleiro[3] and tabuleiro[0] == tabuleiro[6] and tabuleiro[0] != '_': #Verificando coluna 1
        return True
    elif tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] != '_': #Verificando coluna 2
        return True
    elif tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[0] != '_': #Verificando coluna 3
        return True
    elif tabuleiro[0] == tabuleiro[4] and tabuleiro[0] == tabuleiro[8] and tabuleiro[0] != '_': #Verificando diagonal principal
        return True
    elif  tabuleiro[2] == tabuleiro[4] and tabuleiro[2] == tabuleiro[6] and tabuleiro[0] != '_': #Verificando diagonal secundária
        return True
    else:
        return False #Sem vitória naquela rodada
    
def verifica_vitoria_jogador(jogador):
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[0] == tabuleiro[2] and tabuleiro[0] == jogador: #Verificando linha 1
        return True
    elif tabuleiro[3] == tabuleiro[4] and tabuleiro[3] == tabuleiro[5] and tabuleiro[3] == jogador: #Verificando linha 2
        return True
    elif  tabuleiro[6] == tabuleiro[7] and tabuleiro[6] == tabuleiro[8] and tabuleiro[6] == jogador: #Verificando linha 3
        return True
    elif tabuleiro[0] == tabuleiro[3] and tabuleiro[0] == tabuleiro[6] and tabuleiro[0] == jogador: #Verificando coluna 1
        return True
    elif tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] == jogador: #Verificando coluna 2
        return True
    elif tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[0] == jogador: #Verificando coluna 3
        return True
    elif tabuleiro[0] == tabuleiro[4] and tabuleiro[0] == tabuleiro[8] and tabuleiro[0] == jogador: #Verificando diagonal principal
        return True
    elif  tabuleiro[2] == tabuleiro[4] and tabuleiro[2] == tabuleiro[6] and tabuleiro[0] == jogador: #Verificando diagonal secundária
        return True
    else:
        return False #Sem vitória naquela rodada


def verifica_empate():
    for posicao in tabuleiro:
        if posicao == '_': #ainda há jogadas a serem feitas.
            return False
    else:
        return True

def faz_jogada(letra, posicao):
    if verifica_espaco_disponivel(posicao):
        posicao = letra
        if verifica_vitoria():
            if letra == 'x':
                return 'As previsões indicam que o resultado é vitória do x. Aperte o botão correspondente'
            else:
                return 'As previsões indicam que o resultado é vitória do o. Aperte o botão correspondente'
        elif verifica_empate():
            return 'As previsões indicam que o resultado é empate. Aperte o botão correspondente'


def jogada_jogador1(): 
    melhor_placar = -1000
    melhor_jogada = -1

    for posicao in tabuleiro:
        if posicao == '_':
            posicao = jogador1
            placar = minimax(tabuleiro, False)
            posicao = '_'
            if placar > melhor_placar:
                melhor_placar = placar
                melhor_jogada = posicao

    return faz_jogada(jogador1, melhor_jogada)

def jogada_jogador2():
    melhor_placar = 1000
    melhor_jogada = 10

    for posicao in tabuleiro:
        if posicao == '_':
            posicao = jogador2
            placar = minimax(tabuleiro, True)
            posicao = '_'
            if placar < melhor_placar:
                melhor_placar = placar
                melhor_jogada = posicao

    return faz_jogada(jogador2, melhor_jogada)

def minimax(tabuleiro, maximizando):

    if verifica_vitoria_jogador(jogador1):
        return 100 #Jogador que está minimizando (x)
    elif verifica_vitoria_jogador(jogador2):
        return -100 #Jogador que está maximizando (o)
    elif verifica_empate():
        return 0
    else:
        if maximizando:
            melhor_placar = -1000

            for posicao in tabuleiro:
                if posicao == '_':
                    posicao = jogador2
                    placar = minimax(tabuleiro, False)
                    posicao = '_'
                    if placar > melhor_placar:
                        melhor_placar = placar
            return melhor_placar
        
        else:
            melhor_placar = 1000
            for posicao in tabuleiro:
                if posicao == '_':
                    posicao = jogador2
                    placar = minimax(tabuleiro, True)
                    posicao = '_'
                    if placar < melhor_placar:
                        melhor_placar = placar
            return melhor_placar

while not verifica_vitoria():
    jogadas_feitas_j1 = tabuleiro.count('x')
    jogadas_feitas_j2 = tabuleiro.count('o')

    if jogadas_feitas_j1 != jogadas_feitas_j2:
        jogada_jogador2()
    jogada_jogador1()
    jogada_jogador2()