quantidade_jogos = int(input())

time_vencedor = ''
time_perdedor = ''

for i in range(quantidade_jogos):
    nome_time = input()
    numero_gols = int(input())
    numero_chutes_gol = int(input())
    cartoes_amarelo = int(input())
    cartoes_vermelho = int(input())

    total_pontos = (numero_gols * 10) + (numero_chutes_gol * 3) + (cartoes_amarelo * -2) + (cartoes_vermelho * -4)

    if(numero_gols >= (0.3 * numero_chutes_gol)):
        total_pontos += 3
    
    if(cartoes_vermelho >= cartoes_amarelo):
        total_pontos -= 3

    if(i == 0):
        time_vencedor = nome_time
        time_perdedor = nome_time
        utlima_pontuacao = total_pontos
        pontuacao_vencedor = total_pontos

    if(total_pontos > utlima_pontuacao):
        time_vencedor = nome_time
        pontuacao_vencedor = total_pontos
    
    if(total_pontos < 0):
        time_perdedor = nome_time
        print(f'O time {time_perdedor} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
    else:
        if(total_pontos != utlima_pontuacao):
            utlima_pontuacao += total_pontos
            porcentagem_time_vencedor = (pontuacao_vencedor / utlima_pontuacao) * 100
            print(f'Com {porcentagem_time_vencedor:.2f}% dos pontos, o time {time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
        