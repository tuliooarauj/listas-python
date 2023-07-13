penteados = input().split(' - ')
tops = input().split(' - ')
bottoms = input().split(' - ')
sapatos = input().split(' - ')



print('Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!')

decisao = ''

n_mesclagem = 0


while decisao != 'Melhor escolher eu mesma' and decisao != 'Amei!!':

    print('Iniciando mesclagem...')
    n_mesclagem += 1

    modo_giro_secoes = input()
    modo_giro_secoes_splitada = modo_giro_secoes.split()


#===================================================================================================================
 # 1) PARA OS PENTEADOS
#===================================================================================================================
    padrao_split = modo_giro_secoes_splitada[0].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[0]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >
        
        #Zona de foco inicial
        indice_foco_inicial = len(penteados) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) #Retornando o índice da próxima peça de roupa

        if n_mesclagem > 1:
            idx_penteado_escolhindo = penteados.index(penteado_escolhido)
            indice_novo_foco = idx_penteado_escolhindo

        if not len(penteados) == 1:
            distancia_foco_final = abs(indice_novo_foco - (len(penteados) - 1))
            quanto_passado = abs((giro - distancia_foco_final))
            indice_novo_foco = quanto_passado - 1
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        penteado_escolhido = penteados[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[0].split('<')
        

        #Zona de foco inicial
        indice_foco_inicial = len(penteados) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) #Retornando o índice da próxima peça de roupa

        if n_mesclagem > 1:
            idx_penteado_escolhindo = penteados.index(penteado_escolhido)
            indice_novo_foco = idx_penteado_escolhindo
        
        if not len(penteados) == 1:
            distancia_foco_inicial = abs(indice_novo_foco - (len(penteados) - len(penteados)))
            quanto_passado = abs((giro - distancia_foco_inicial))
            indice_novo_foco = quanto_passado
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0
        

        penteado_escolhido = penteados[indice_novo_foco]
#===================================================================================================================
 # 2) PARA OS TOPS
#===================================================================================================================

    padrao_split = modo_giro_secoes_splitada[1].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[1]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >

        #Zona de foco inicial
        indice_foco_inicial = len(tops) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 
        
        if n_mesclagem > 1:
            idx_top_escolhindo = tops.index(top_escolhido)
            indice_novo_foco = idx_top_escolhindo

        if not len(tops) == 1:
            distancia_foco_final = abs(indice_novo_foco - (len(tops) - 1))
            quanto_passado = abs((giro - distancia_foco_final))
            indice_novo_foco = quanto_passado - 1
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        top_escolhido = tops[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[1].split('<')

        #Zona de foco inicial
        indice_foco_inicial = len(tops) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0])

        if n_mesclagem > 1:
            idx_top_escolhindo = tops.index(top_escolhido)
            indice_novo_foco = idx_top_escolhindo 
        
        if not len(tops) == 1:
            distancia_foco_inicial = abs(indice_novo_foco - (len(tops) - len(tops)))
            quanto_passado = abs((giro - distancia_foco_inicial))
            indice_novo_foco = quanto_passado
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        top_escolhido = tops[indice_novo_foco]

#===================================================================================================================
 # 3) PARA OS BOTTOMS
#===================================================================================================================

    padrao_split = modo_giro_secoes_splitada[2].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[2]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >

        #Zona de foco inicial
        indice_foco_inicial = len(bottoms) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 

        if n_mesclagem > 1:
            idx_bottom_escolhindo = bottoms.index(bottom_escolhido)
            indice_novo_foco = idx_bottom_escolhindo
        
        if not len(bottoms) == 1:
            distancia_foco_final = abs(indice_novo_foco - (len(bottoms) - 1))
            quanto_passado = abs((giro - distancia_foco_final))
            indice_novo_foco = quanto_passado - 1   
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        bottom_escolhido = bottoms[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[2].split('<')

        #Zona de foco inicial
        indice_foco_inicial = len(bottoms) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 

        if n_mesclagem > 1:
            idx_bottom_escolhindo = bottoms.index(bottom_escolhido)
            indice_novo_foco = idx_bottom_escolhindo
        
        if not len(bottoms) == 1:  
            distancia_foco_inicial = abs(indice_novo_foco - (len(bottoms) - len(bottoms)))
            quanto_passado = abs((giro - distancia_foco_inicial))
            indice_novo_foco = quanto_passado
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        bottom_escolhido = bottoms[indice_novo_foco]

#===================================================================================================================
 # 3) PARA OS SAPATOS
#===================================================================================================================

    padrao_split = modo_giro_secoes_splitada[3].split('>') #SUPOSIÇÃO
    if not padrao_split[0] == modo_giro_secoes_splitada[3]: #CONSEGUIU SPLITAR
        #PARA A DIREITA >

        #Zona de foco inicial
        indice_foco_inicial = len(sapatos) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 

        if n_mesclagem > 1:
            idx_sapato_escolhindo = sapatos.index(sapato_escolhido)
            indice_novo_foco = idx_sapato_escolhindo
        

        if not len(sapatos) == 1:
            distancia_foco_final = abs(indice_novo_foco - (len(sapatos) - 1))
            quanto_passado = abs((giro - distancia_foco_final))
            indice_novo_foco = quanto_passado - 1  
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        sapato_escolhido = sapatos[indice_novo_foco]


    else: #NAO CONSEGUIU SPLITAR

        #PARA A ESQUERDA <
        padrao_split = modo_giro_secoes_splitada[3].split('<')

        #Zona de foco inicial
        indice_foco_inicial = len(sapatos) // 2
        if n_mesclagem == 1:
            indice_novo_foco = indice_foco_inicial
        #Giro da máquina
        giro = int(padrao_split[0]) 

        if n_mesclagem > 1:
            idx_sapato_escolhindo = sapatos.index(sapato_escolhido)
            indice_novo_foco = idx_sapato_escolhindo
        
        if not len(penteados) == 1:
            distancia_foco_inicial = abs(indice_novo_foco - (len(sapatos) - len(sapatos)))
            quanto_passado = abs((giro - distancia_foco_inicial))
            indice_novo_foco = quanto_passado   
        else:  #caso da entrada só ter 1 elemento
            indice_novo_foco = 0

        sapato_escolhido = sapatos[indice_novo_foco]


    print('O look gerado foi:')
    print(f'cabelo {penteado_escolhido}, {top_escolhido} com {bottom_escolhido} e {sapato_escolhido} nos pés.')

    decisao = input()

    if decisao == 'Amei!!' and top_escolhido == 'camisa da seleção':
        print('Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!')
    elif decisao == 'Amei!!' and top_escolhido != 'camisa da seleção':
        print('Essa Barbie vai arrasar com o look perfeito!')
    elif decisao == 'Melhor escolher eu mesma':
       print('Acho que estou precisando de ajustes, Ken :(') 

