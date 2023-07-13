qtd_ideal_treino = int(input())
qtd_entradas_seguintes = int(input())
relacao_posicao_treino = []
minutos_posicao = []

for entrada in range(qtd_entradas_seguintes):
    posicao_min_treino = input().split(' ')   
    relacao_posicao_treino.append(posicao_min_treino)
for relacao in relacao_posicao_treino:
        minutos_posicao.append(int(relacao[1]))

if len(minutos_posicao) == 1:
    if minutos_posicao[0] == qtd_ideal_treino:
     print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao_posicao_treino[0][0]}!')

if len(minutos_posicao) > 1:
    lista_resultado = []
    for idx in range(1, qtd_entradas_seguintes):
        if idx == 1:
            soma_treinamento = minutos_posicao[0] + minutos_posicao[idx]
            if soma_treinamento == qtd_ideal_treino:
                lista_resultado.append(relacao_posicao_treino[idx][0])
                print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao_posicao_treino[idx][0]}!')
        if idx > 1:
            soma_treinamento += minutos_posicao[idx]
            if soma_treinamento == qtd_ideal_treino:
                print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao[0]}!')




