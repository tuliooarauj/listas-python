frase_informada = ''

caso_1 = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
caso_2 = 'Encham o cooler, vai começar um jogo!!!!'
caso_3 = 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário'
caso_4 = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

estoque = 20

while(estoque >= 0 and frase_informada != caso_4):

    frase_informada = input()
    
    if(frase_informada == caso_1):
        jogadores_saida = int(input())
        if(estoque < jogadores_saida):
            print(f'Não teremos água para todos os jogadores... Temos que garantir {jogadores_saida - estoque} garrafas!!')
            estoque *= 2
            estoque -= jogadores_saida
        else:
            estoque -= jogadores_saida
    else:
        if(frase_informada == caso_2):
            estoque += 15
            print('Geladeira cheia!')
        else:
            if(frase_informada == caso_3):
                quantidade_1 = int(input())
                quantidade_2 = int(input())
                quantidade_3 = int(input())
                quantidade_4 = int(input())
                quantidade_5 = int(input())

                total_garrafas = quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5

                estoque -= total_garrafas
                if(estoque < 0):
                    print(f'Prometemos distribuir {abs(estoque)} garrafas e zeramos')
    

                

else:
    if(estoque < 0):
        print('Por questões logísticas, teremos que acabar com os jogos...')
        if(frase_informada == caso_4):
            print(f'Estamos devendo {abs(estoque)} garrafas para os alunos...')
    elif(frase_informada == caso_4):
        if(estoque == 0):
            print('Vendemos todas as águas, fizemos uma contagem certeira!!')
        if(estoque > 0):
            print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')