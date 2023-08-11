def cria_mapa(tam_mapa):
    mapa_sala = []
    for _ in range(tam_mapa):
        sublista = input()
        mapa_sala.append(sublista)
    return mapa_sala

def encontra_prox_sala(sala):
    str_sala = ''.join(sala) #concatenando a lista numa string
    elemento = str_sala[:1]
    if sala is None:
        fim = True
        return fim
    if elemento.isnumeric():
        return elemento
    else:
        return encontra_prox_sala(str_sala[1:])
    

def desbrava_castelo(matriz_castelo, idx_sala):
    if len(matriz_castelo) == 0:
        return matriz_castelo
    else:
        sala_atual = matriz_castelo[int(idx_sala)]
        matriz_castelo[int(idx_sala)] = []
        return desbrava_castelo(matriz_castelo, encontra_prox_sala(sala_atual))
    

'''def conta_moeda()'''


quantidade_salas = int(input())
mapa_castelo = cria_mapa(quantidade_salas)
sala_inicial = int(input())

desbrava_castelo(mapa_castelo, sala_inicial)

