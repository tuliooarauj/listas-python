acao_feita = input()

acao1 = 'Explorar arara'
acao2 = 'Meninas, acho que já falei demais. Vamos para o shopping?'

numero_arara = 0
while acao_feita != acao2:
    lista_profissoes_fora = []
    qtd_diferentes = 0
    print(f'Arara {numero_arara}:')

    conteudo_arara = []
    conteudo_arara = input().split(', ')
    
    profissoes_faladas = []
    profissoes_faladas = input().split(', ')

    for profissoes_arara in conteudo_arara:    
        if not profissoes_faladas.count(profissoes_arara):
            qtd_diferentes += 1
            profissao_fora = conteudo_arara.pop(conteudo_arara.index(profissoes_arara))
            lista_profissoes_fora.append(profissao_fora)
            conteudo_arara.insert(0,profissao_fora)

    if len(conteudo_arara) != len(profissoes_faladas):
        print('Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!')
    else:
        if qtd_diferentes > 0:
            total_profissoes_fora = ', '.join(lista_profissoes_fora)
            print(f'Poxa, Barbie! Você acabou desorganizando essa arara, e {qtd_diferentes} profissões vão ficar de fora da conversa. São elas: {total_profissoes_fora}.')
    

    for profissoes in profissoes_faladas:
        if not conteudo_arara.count(profissoes):
            qtd_diferentes += 1
    if qtd_diferentes == 0:
        print('Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!')
        
    acao_feita = input()
    numero_arara += 1

