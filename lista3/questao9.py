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

idx = 0
lista_resultado = []
while idx < qtd_entradas_seguintes: 

    if idx == qtd_entradas_seguintes:
        qtd_entradas_seguintes -= 1
        relacao_posicao_treino.pop(0)
        lista_resultado = []
        idx = 0

    if idx == 0:
        somatorio = minutos_posicao[0]
        lista_resultado.append(relacao_posicao_treino[idx][0])
        relacao_somatorio = ' '.join(lista_resultado)
        if somatorio == qtd_ideal_treino:
            print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao_somatorio}!')
            venceu = True

    else:
        somatorio += minutos_posicao[idx]
        lista_resultado.append(relacao_posicao_treino[idx][0])
        relacao_somatorio = ' '.join(lista_resultado)
        if somatorio == qtd_ideal_treino:
            print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {relacao_somatorio}!')
            venceu = True

    idx += 1

if not venceu:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')    