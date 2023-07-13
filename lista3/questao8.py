penteados = input().split(' - ')
tops = input().split(' - ')
bottoms = input().split(' - ')
sapatos = input().split(' - ')

modo_giro_secoes = input()
modo_giro_secoes_splitada = modo_giro_secoes.split()

print('Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!')

decisao = ''

n_mesclagem = 0


while decisao != 'Melhor escolher eu mesma':

    print('Iniciando mesclagem...')
    n_mesclagem += 1

#===================================================================================================================
 # 1) PARA OS PENTEADOS
#===================================================================================================================
    padrao_split = modo_giro_secoes_splitada[0].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[0]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >
        num_giros = padrao_split[0]

        #Zona de foco inicial
        indice_foco_inicial = len(penteados) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) #Retornando o índice da próxima peça de roupa
        
        distancia_foco_final = abs(indice_novo_foco - (len(penteados) - 1))
        quanto_passado = abs((giro - distancia_foco_final))
        indice_novo_foco = quanto_passado - 1

        penteado_escolhido = penteados[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[0].split('<')
        num_giros = padrao_split[0]

        #Zona de foco inicial
        indice_foco_inicial = len(penteados) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) #Retornando o índice da próxima peça de roupa
        
        distancia_foco_inicial = abs(indice_novo_foco - (len(penteados) - len(penteados)))
        quanto_passado = abs((giro - distancia_foco_inicial))
        indice_novo_foco = quanto_passado

        penteado_escolhido = penteados[indice_novo_foco]
#===================================================================================================================
 # 2) PARA OS TOPS
#===================================================================================================================

    padrao_split = modo_giro_secoes_splitada[1].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[1]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >
        num_giros = padrao_split[1]

        #Zona de foco inicial
        indice_foco_inicial = len(penteados) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 
        
        distancia_foco_final = abs(indice_novo_foco - (len(tops) - 1))
        quanto_passado = abs((giro - distancia_foco_final))
        indice_novo_foco = quanto_passado - 1

        top_escolhido = tops[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[1].split('<')
        num_giros = padrao_split[1]

        #Zona de foco inicial
        indice_foco_inicial = len(tops) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 
        
        distancia_foco_inicial = abs(indice_novo_foco - (len(tops) - len(tops)))
        quanto_passado = abs((giro - distancia_foco_inicial))
        indice_novo_foco = quanto_passado

        top_escolhido = tops[indice_novo_foco]

#===================================================================================================================
 # 3) PARA OS BOTTOMS
#===================================================================================================================


