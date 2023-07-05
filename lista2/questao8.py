equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()

quantidade_partidas = int(input())

pontos_totais_equipe1 = 0
pontos_totais_equipe2 = 0
vitoria_equipe1 = 0
vitoria_equipe2 = 0

i = 0

print(f'VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:')
print(f'{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}')

while(i < quantidade_partidas):
    i+=1

    pontuacao_equipe1 = int(input())
    pontuacao_equipe2 = int(input())

    pontos_totais_equipe1 += pontuacao_equipe1
    pontos_totais_equipe2 += pontuacao_equipe2

    if(pontuacao_equipe1 >= pontuacao_equipe2):
        vitoria_equipe1 += 1
    else:
        vitoria_equipe2 += 1
    

    if(pontuacao_equipe1 == 0 or pontuacao_equipe2 == 0):
        if(pontuacao_equipe1 == 0):
            print('JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA')
            quantidade_partidas = 0
        else:
            print('JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA')
            quantidade_partidas = 0

if(pontuacao_equipe1 > 0 and pontuacao_equipe2 > 0):
    pontuacao_geral_equipe1 = pontos_totais_equipe1 * (vitoria_equipe1/quantidade_partidas)
    pontuacao_geral_equipe2 = pontos_totais_equipe2 * (vitoria_equipe2/quantidade_partidas)

    if(pontuacao_geral_equipe1 >= pontuacao_geral_equipe2):
        print(f'CARAMBA! Tivemos um total de {pontos_totais_equipe1 + pontos_totais_equipe2} bolas ao chão ao longo dessa disputa.')
        print(f'{equipe1_nome1} e {equipe1_nome2} são os grandes vencedores!')
        print(f'Mataram {pontos_totais_equipe1} bolas, ganhando {vitoria_equipe1} partidas')
    else:
        print(f'CARAMBA! Tivemos um total de {pontos_totais_equipe1 + pontos_totais_equipe2} bolas ao chão ao longo dessa disputa.')
        print(f'{equipe2_nome1} e {equipe2_nome2} são os grandes vencedores!')
        print(f'Mataram {pontos_totais_equipe2} bolas, ganhando {vitoria_equipe2} partidas')