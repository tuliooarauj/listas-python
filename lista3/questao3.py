numero_colecoes = int(input())
colecao = []
notas = []

peca_indesejada1 = ['colete preto', 'coturno']
peca_indesejada2 = ['vestido com babados' , 'blusa bufante']



for i in range(numero_colecoes):
    peca_indesejada = False
    nota_atual = 0
    colecao = input().split(', ')
    notas = input().split(', ')
    
    for peca in colecao:
        if not peca_indesejada:
            for indesejada in peca_indesejada1:
                if peca == indesejada:
                    peca_indesejada = True
                    print(f'{indesejada} é uma peça muito gótica, não faz o estilo da Glimmer.')
        if not peca_indesejada:
            for indesejada in peca_indesejada2:
                if peca == indesejada:
                    peca_indesejada = True
                    print(f'{indesejada} é uma peça muito antiquada, infelizmente essa coleção não vai servir...')

    if not peca_indesejada:
        for nota in notas:
            nota_atual += int(nota)

        if nota_atual / len(notas) >= 6:
            print('Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar')
        else:
            print('Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.')

