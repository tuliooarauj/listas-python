time_1 = input()
time_2 = input()

n_rodada = 1
vitorias_time_1 = 0
vitorias_time_2 = 0

while(vitorias_time_1 != 3 and vitorias_time_2 != 3):
    pontuacao_time_1 = int(input())
    pontuacao_time_2 = int(input())
    
    if(pontuacao_time_1 > pontuacao_time_2):
        print(f'O vencedor da {n_rodada}ª rodada foi: {time_1}')
        vitorias_time_1 += 1
    else:
        print(f'O vencedor da {n_rodada}ª rodada foi: {time_2}')
        vitorias_time_2 += 1
    n_rodada += 1

if(vitorias_time_1 == 3):
    print(f'O time {time_1} ganhou a partida final!')
elif(vitorias_time_2 == 3):
    print(f'O time {time_2} ganhou a partida final!')