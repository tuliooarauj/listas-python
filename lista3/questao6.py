acao1 = 'Quero adicionar um item'
acao2 = 'Quero remover um item'
acao3 = 'Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?'
acao4 = 'Fim! Muito obrigada pela ajuda!!'

restricoes = []
restricoes = input().split(' ; ')
qtd_objetos = 0

qtd_maxima_objetos = int(restricoes[0])
custo_maximo = int(restricoes[1])

while qtd_objetos < qtd_maxima_objetos:

    acao_desejada = input()

    if acao_desejada == acao4:
        print('Por nada! Estou sempre à disposição!')
    else:
        if acao_desejada == acao1: 
            
        