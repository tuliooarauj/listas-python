qtd_partidas = int(input())

i = 0

while(i <= qtd_partidas):
    i += 1
    placar_equipe = 0
    placar_adversario = 0
    qtd_rodadas = int(input())
    if(i< qtd_partidas):
        print(f'Vai começar a {i}º partida. Esse jogo terá {qtd_rodadas} rodada(s).')
    for j in range(qtd_rodadas):
        habilidade_jogador = int(input())
        habilidade_adversario = int(input())

        if(habilidade_jogador >= habilidade_adversario):
            placar_equipe += 1
        else:
            placar_adversario += 1
    if(i < qtd_partidas):
        print(f'Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}')
        if(placar_adversario == placar_equipe):
            qtd_partidas = 0
            print('Não foi dessa vez! Treinar pro ano que vem!')
        elif(placar_equipe >= placar_adversario + 5 and i < qtd_partidas):
            print('QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!')
            qtd_partidas = 0
        else:
            print('Vamos para próxima fase!')  
      
    if(i == qtd_partidas):
        print(f'Tá na hora da grande final! Esse jogo terá {qtd_rodadas} rodada(s).')
        print(f'Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}')
        if(placar_equipe <= placar_adversario):
            print('Ah não!! Chegaram tão longe mas não foi dessa vez. :(')
            qtd_partidas = 0
        else:
            print('É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!')
            qtd_partidas = 0