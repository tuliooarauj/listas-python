n_participantes  = int(input())

for i in range(n_participantes):
        
    nome_participante = input()
    pontuacao = int(input())
    penalidade = int(input())
    pontuacao_total = pontuacao - penalidade
    
    if(i==0):
        maior_pontuacao_total = pontuacao_total
        nome_ganhador = nome_participante

    if(pontuacao_total > maior_pontuacao_total):
        maior_pontuacao_total = pontuacao_total
        nome_ganhador = nome_participante

print(f'O grande vencedor do torneio foi {nome_ganhador} com um total de {maior_pontuacao_total} pontos!')

