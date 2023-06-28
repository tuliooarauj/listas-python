quantidade_duplas = int(input())

for i in range(quantidade_duplas):
    nome_duplas = input()
    periodo_duplas = int(input())
    pontos_duplas = int(input())
    pontuacao_final = pontos_duplas / periodo_duplas

    if(i==0):
        maior_pontuacao = pontuacao_final
        menor_pontuacao = pontuacao_final
        dupla_vencedora = nome_duplas
        dupla_perdedora = nome_duplas

    if(pontuacao_final > maior_pontuacao):
        maior_pontuacao = pontuacao_final
        dupla_vencedora = nome_duplas
    
    if(pontuacao_final < menor_pontuacao):
        menor_pontuacao = pontuacao_final
        dupla_perdedora = nome_duplas
        

print(f'A dupla vencedora foi {dupla_vencedora} com a pontuação final de {maior_pontuacao:.2f} pontos.')
print(f'A dupla perdedora foi {dupla_perdedora} com a pontuação final de {menor_pontuacao:.2f} pontos.')