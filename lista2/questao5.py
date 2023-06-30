quantidade_jogos = int(input())

time_vencedor = ''
time_perdedor = ''
total_pontos = 0
pontos_manchester = 0
pontos_spicin = 0

for i in range(quantidade_jogos):
    if(pontos_manchester >= 0 and pontos_spicin >= 0):
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

        for _ in range(nome_time == 'Manchester CIn'):
            pontos_manchester += total_pontos

        for _ in range(nome_time == 'SpiCIn Girls'):
            pontos_spicin += total_pontos

        soma_pontuacao = pontos_spicin + pontos_manchester

        if(pontos_manchester > pontos_spicin):
            time_vencedor = 'Manchester CIn'
            pontuacao_vencedor = pontos_manchester
        else:
            time_vencedor = 'SpiCIn Girls'
            pontuacao_vencedor = pontos_spicin

        if(pontos_spicin < 0 or pontos_manchester < 0):
            time_perdedor = nome_time
            print(f'O time {time_perdedor} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
           
if(pontos_manchester != pontos_spicin) and (pontos_manchester >= 0 and pontos_spicin >= 0):
    if(quantidade_jogos == 1 and pontuacao_vencedor > 0):
        porcentagem_time_vencedor = (pontuacao_vencedor / pontuacao_vencedor) * 100        
        print(f'Com {porcentagem_time_vencedor:.2f}% dos pontos, o time {time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
    else:
        porcentagem_time_vencedor = (pontuacao_vencedor / soma_pontuacao) * 100        
        print(f'Com {porcentagem_time_vencedor:.2f}% dos pontos, o time {time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
        