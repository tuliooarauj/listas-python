entrou_top = 0
entrou_jungler = 0
entrou_mid = 0
entrou_adc = 0
entrou_suporte = 0

time = 0

cont_artur = 0
cont_frej = 0
pts_time = 0
entrada = 0

while(time != 5):
    entrada += 1
    nome_jogador = input()
    lane_jogador = input()
    elo_jogador = input()

    if(nome_jogador == 'Bruna'):
        print('LOL NÃO!!! TUDO MENOS LOL!!!')
        time = 6
    else:
        if(elo_jogador == 'bronze' or elo_jogador == 'prata' or elo_jogador == 'ouro' or elo_jogador == 'platina' or elo_jogador == 'diamante' or elo_jogador == 'desafiante'):
            print('Não conheço esse elo, então vou considerar que é um elo ruim.')
            pts_time += 0
        else:
            if(lane_jogador == 'Top' and entrou_top == 0):
                print(f'{nome_jogador} entrou pro time.')
                relacao_top = (f'{nome_jogador} - {lane_jogador} ({elo_jogador})')
                entrou_top += 1
                entrada_top = entrada
                if(elo_jogador == 'Bronze'):
                    pts_time += 1
                if(elo_jogador == 'Prata'):
                    pts_time += 2
                if(elo_jogador == 'Ouro'):
                    pts_time += 4
                if(elo_jogador == 'Platina'):
                    pts_time += 6
                if(elo_jogador == 'Diamante'):
                    pts_time += 8
                if(elo_jogador == 'Desafiante'):
                    pts_time += 10
            else:
                if(lane_jogador == 'Top' and entrou_top == 1):
                    print(f'{nome_jogador} não foi aceito, que pena.')
            
            if(lane_jogador == 'Jungler' and entrou_jungler == 0):
                print(f'{nome_jogador} entrou pro time.')
                relacao_jungler = (f'{nome_jogador} - {lane_jogador} ({elo_jogador})')
                entrou_jungler += 1
                entrada_jungler = entrada
                if(elo_jogador == 'Bronze'):
                    pts_time += 1
                if(elo_jogador == 'Prata'):
                    pts_time += 2
                if(elo_jogador == 'Ouro'):
                    pts_time += 4
                if(elo_jogador == 'Platina'):
                    pts_time += 6
                if(elo_jogador == 'Diamante'):
                    pts_time += 8
                if(elo_jogador == 'Desafiante'):
                    pts_time += 10


            else:
                if(lane_jogador == 'Jungler' and entrou_jungler == 1):
                    print(f'{nome_jogador} não foi aceito, que pena.')

            if(lane_jogador == 'Mid' and entrou_mid == 0):
                print(f'{nome_jogador} entrou pro time.')
                relacao_mid = (f'{nome_jogador} - {lane_jogador} ({elo_jogador})')
                entrou_mid += 1
                entrada_mid = entrada
                if(elo_jogador == 'Bronze'):
                    pts_time += 1
                if(elo_jogador == 'Prata'):
                    pts_time += 2
                if(elo_jogador == 'Ouro'):
                    pts_time += 4
                if(elo_jogador == 'Platina'):
                    pts_time += 6
                if(elo_jogador == 'Diamante'):
                    pts_time += 8
                if(elo_jogador == 'Desafiante'):
                    pts_time += 10
            else:
                if(lane_jogador == 'Mid' and entrou_mid == 1):
                    print(f'{nome_jogador} não foi aceito, que pena.')

            if(lane_jogador == 'Adc' and entrou_adc == 0):
                print(f'{nome_jogador} entrou pro time.')
                relacao_adc = (f'{nome_jogador} - {lane_jogador} ({elo_jogador})')
                entrou_adc += 1
                entrada_adc = entrada
                if(elo_jogador == 'Bronze'):
                    pts_time += 1
                if(elo_jogador == 'Prata'):
                    pts_time += 2
                if(elo_jogador == 'Ouro'):
                    pts_time += 4
                if(elo_jogador == 'Platina'):
                    pts_time += 6
                if(elo_jogador == 'Diamante'):
                    pts_time += 8
                if(elo_jogador == 'Desafiante'):
                    pts_time += 10
            else:
                if(lane_jogador == 'Adc' and entrou_adc == 1):
                    print(f'{nome_jogador} não foi aceito, que pena.')

            if(lane_jogador == 'Suporte' and entrou_suporte == 0):
                print(f'{nome_jogador} entrou pro time.')
                relacao_suporte = (f'{nome_jogador} - {lane_jogador} ({elo_jogador})')
                entrou_suporte += 1
                entrada_suporte = entrada
                if(elo_jogador == 'Bronze'):
                    pts_time += 1
                if(elo_jogador == 'Prata'):
                    pts_time += 2
                if(elo_jogador == 'Ouro'):
                    pts_time += 4
                if(elo_jogador == 'Platina'):
                    pts_time += 6
                if(elo_jogador == 'Diamante'):
                    pts_time += 8
                if(elo_jogador == 'Desafiante'):
                    pts_time += 10
            else:
                if(lane_jogador == 'Suporte' and entrou_suporte == 1):
                    print(f'{nome_jogador} não foi aceito, que pena.')