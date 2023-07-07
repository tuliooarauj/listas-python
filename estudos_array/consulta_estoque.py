produtos_vendidos = ['martelo', 'tesoura', 'chave de fenda', 'prego', 'chave estrela']
produtos_estoque = ['martelo', 'tesoura', 'tesoura', 'martelo', 'prego', 'prego', 'martelo']

for prod_vendido in produtos_vendidos:
    qtd_estoque = 0
    for prod_estoque in produtos_estoque:
        if prod_vendido == prod_estoque:
            qtd_estoque += 1

    print(f'O produto {prod_vendido} possui {qtd_estoque} unidade(s) no estoque.')
