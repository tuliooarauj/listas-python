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

while(time < 5):
    entrada += 1
    nome_jogador = input()

    if(nome_jogador == 'Bruna'):
        print('LOL NÃO!!! TUDO MENOS LOL!!!')
        time = 6
    else:
        lane_jogador = input()
        elo_jogador = input()

        if(elo_jogador != 'Bronze' and elo_jogador != 'Prata' and elo_jogador != 'Ouro' and elo_jogador != 'Platina' and elo_jogador != 'Diamante' and elo_jogador != 'Desafiante'):
            print('Não conheço esse elo, então vou considerar que é um elo ruim.')
        
        if(lane_jogador == 'Top' and entrou_top == 0):
            print(f'{nome_jogador} entrou pro time.')
            if(nome_jogador == 'Artur'):
                print('Ele tá meio enferrujado...')
                cont_artur +=1
            if(nome_jogador == 'Frej'):
                print('Joga muito!')
                cont_frej += 1
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
            if(nome_jogador == 'Artur'):
                print('Ele tá meio enferrujado...')
                cont_artur +=1
            if(nome_jogador == 'Frej'):
                print('Joga muito!')
                cont_frej += 1
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
            if(nome_jogador == 'Artur'):
                print('Ele tá meio enferrujado...')
                cont_artur +=1
            if(nome_jogador == 'Frej'):
                print('Joga muito!')
                cont_frej += 1
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
            if(nome_jogador == 'Artur'):
                print('Ele tá meio enferrujado...')
                cont_artur +=1
            if(nome_jogador == 'Frej'):
                print('Joga muito!')
                cont_frej += 1
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
            if(nome_jogador == 'Artur'):
                print('Ele tá meio enferrujado...')
                cont_artur +=1
            if(nome_jogador == 'Frej'):
                print('Joga muito!')
                cont_frej += 1
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

       
    
        time = entrou_top + entrou_jungler + entrou_mid + entrou_adc + entrou_suporte

        
        
        if(time == 5):
            print('O time está completo.')
            #top, mid, jungler, adc, suporte
            
            primeiro = min(entrada_top, entrada_mid, entrada_jungler, entrada_adc, entrada_suporte)

            segundo = None
            for num in (entrada_top, entrada_mid, entrada_jungler, entrada_adc, entrada_suporte):
                if num != primeiro:
                    if segundo is None or num < segundo:
                        segundo = num

            terceiro = None
            for num in (entrada_top, entrada_mid, entrada_jungler, entrada_adc, entrada_suporte):
                if num != primeiro and num != segundo:
                    if terceiro is None or num < terceiro:
                        terceiro = num 

            quarto = None
            for num in (entrada_top, entrada_mid, entrada_jungler, entrada_adc, entrada_suporte):
                if num != primeiro and num != segundo and num != terceiro:
                    if quarto is None or num < quarto:
                        quarto = num

            ultimo = max(entrada_top, entrada_mid, entrada_jungler, entrada_adc, entrada_suporte)

            if(primeiro == entrada_top):
                print(relacao_top)
            if(primeiro == entrada_mid):
                print(relacao_mid)
            if(primeiro == entrada_jungler):
                print(relacao_jungler)
            if(primeiro == entrada_adc):
                print(relacao_adc)
            if(primeiro == entrada_suporte):
                print(relacao_suporte)

            if(segundo == entrada_top):
                print(relacao_top)
            if(segundo == entrada_mid):
                print(relacao_mid)
            if(segundo == entrada_jungler):
                print(relacao_jungler)
            if(segundo == entrada_adc):
                print(relacao_adc)
            if(segundo == entrada_suporte):
                print(relacao_suporte)
            
            if(terceiro == entrada_top):
                print(relacao_top)
            if(terceiro == entrada_mid):
                print(relacao_mid)
            if(terceiro == entrada_jungler):
                print(relacao_jungler)
            if(terceiro == entrada_adc):
                print(relacao_adc)
            if(terceiro == entrada_suporte):
                print(relacao_suporte)
            
            if(quarto == entrada_top):
                print(relacao_top)
            if(quarto == entrada_mid):
                print(relacao_mid)
            if(quarto == entrada_jungler):
                print(relacao_jungler)
            if(quarto == entrada_adc):
                print(relacao_adc)
            if(quarto == entrada_suporte):
                print(relacao_suporte)

            if(ultimo == entrada_top):
                print(relacao_top)
            if(ultimo == entrada_mid):
                print(relacao_mid)
            if(ultimo == entrada_jungler):
                print(relacao_jungler)
            if(ultimo == entrada_adc):
                print(relacao_adc)
            if(ultimo == entrada_suporte):
                print(relacao_suporte)

            if(cont_artur == 1) and (cont_frej == 0):
                print('Vai dar ruim...')
            elif(cont_artur == 0) and (cont_frej == 1):
                print('A GENTE VAI GANHAR!!!')
            else:
                if((cont_artur == 1) and (cont_frej == 1)) or ((cont_artur == 0) and (cont_frej == 0)):
                    if(pts_time >= 18):
                        print('A GENTE VAI GANHAR!!!')
                    else:
                        print('Vai dar ruim...')

                    
                
                    

                

            
