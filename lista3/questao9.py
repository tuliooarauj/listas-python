qtd_ideal_treino = int(input())
qtd_entradas_seguintes = int(input())
relacao_posicao_treino = []
minutos_posicao = []

venceu = False

for entrada in range(qtd_entradas_seguintes):
    posicao_min_treino = input().split(' ')   
    relacao_posicao_treino.append(posicao_min_treino)
for relacao in relacao_posicao_treino:
        minutos_posicao.append(int(relacao[1]))

for num in range(qtd_entradas_seguintes, -1, -1):
    if num == qtd_entradas_seguintes:
        fat = num - 0
    if num != qtd_entradas_seguintes:
        fat += num



if len(minutos_posicao) == 1:
    if minutos_posicao[0] == qtd_ideal_treino:
        venceu = True 
        print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao_posicao_treino[0][0]}!')

if len(minutos_posicao) > 1:
    lista_resultado = []
    for idx in range(1, qtd_entradas_seguintes): #range !qtd_entradas
        if idx == 1:
            soma_treinamento = minutos_posicao[0] + minutos_posicao[idx]
            lista_resultado.append(relacao_posicao_treino[0][0])
            if soma_treinamento == qtd_ideal_treino:
                lista_resultado.append(relacao_posicao_treino[idx][0])
                venceu = True
                print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {lista_resultado}')

        if idx > 1:
            lista_resultado.append(relacao_posicao_treino[1][0])
            soma_treinamento += minutos_posicao[idx]
            if soma_treinamento == qtd_ideal_treino:
                lista_resultado.append(relacao_posicao_treino[idx][0])
                venceu = True
                print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {lista_resultado}')

if not venceu:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')    