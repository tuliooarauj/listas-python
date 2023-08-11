def cria_mapa(tam_mapa):
    mapa_sala = []
    for _ in range(tam_mapa):
        sublista = input()
        mapa_sala.append(sublista)
    return mapa_sala

def encontra_prox_sala(sala):
    elemento = sala[:1] #encontrando o numero da sala por slicing
    if elemento.isnumeric():
        return int(elemento) #idx da prox sala
    else:
        return encontra_prox_sala(sala[1:])

def conta_moeda_sala(sala, qtd_moeda):
    if sala[:1] == '': #encontrando as moedas por slicing
        return qtd_moeda
    else:
        if sala[:1] == '◇':
            qtd_moeda += 1
        return conta_moeda_sala(sala[1:], qtd_moeda)

def encontra_espada(sala, espada_encontrada): 
    if sala == '':
        return espada_encontrada
    else:
        if sala[:len('espada')] == 'espada':
            espada_encontrada = True
            return espada_encontrada
        else:
            return encontra_espada(sala[1:], espada_encontrada)

def encontra_zelda(sala): 
    if sala == '':
        return False
    else:
        if sala[:len('Zelda')] == 'Zelda':
            return True
        else:
            return encontra_zelda(sala[1:])
        
def encontra_agahnim(sala): 
    if sala == '':
        return False
    else:
        if sala[:len('Agahnim')] == 'Agahnim':
            return True
        else:
            return encontra_agahnim(sala[1:])

def desbrava_castelo(matriz_castelo, idx_sala, encontrou_princesa, qtd_moeda, encontrou_espada, encontrou_agahnim):
    if encontrou_princesa == True:
        return True, encontrou_espada, encontrou_agahnim, qtd_moeda
    elif matriz_castelo[idx_sala] == []:
        return False, qtd_moeda
    else:
        sala_atual = matriz_castelo[int(idx_sala)]
        matriz_castelo[int(idx_sala)] = []
        return desbrava_castelo(matriz_castelo, encontra_prox_sala(sala_atual), encontra_zelda(sala_atual), conta_moeda_sala(sala_atual, qtd_moeda), encontra_espada(sala_atual, encontrou_espada), encontra_agahnim(sala_atual))



quantidade_salas = int(input())
matriz_castelo = cria_mapa(quantidade_salas)
mapa_castelo = matriz_castelo.copy()
sala_inicial = int(input())
moedas_iniciais = 0
princesa_encontrada = False
espada_encontrada = False
agahnim_encontrado = False

print(desbrava_castelo(matriz_castelo, sala_inicial, princesa_encontrada, moedas_iniciais, espada_encontrada, agahnim_encontrado))
#print(moedas_castelo(mapa_castelo, moedas_iniciais))
