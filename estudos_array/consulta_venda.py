produtos_vendidos = ['martelo', 'tesoura', 'chave de fenda', 'prego', 'chave estrela']
produtos_estoque = ['martelo', 'tesoura', 'tesoura', 'martelo', 'prego', 'prego', 'martelo']

produto = input()

vende_produto = False

for prod_vendido in produtos_vendidos:
    if prod_vendido == produto:
        vende_produto = True
    
if vende_produto:
    print(f'O produto {produto} é vendido nessa loja.')

    qtd_produto = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == produto:
            qtd_produto += 1

    if qtd_produto == 0:
        print('Porém, não está disponível no estoque.')
    else:
        print(f'A quantidade em estoque de {produto} é {qtd_produto}.')
else:
    print('Essa loja não vende esse produto.')

