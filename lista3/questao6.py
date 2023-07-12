acao1 = 'Quero adicionar um item'
acao2 = 'Quero remover um item'
acao3 = 'Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?'
acao4 = 'Fim! Muito obrigada pela ajuda!!'

restricoes = []
restricoes = input().split(' ; ')

qtd_maxima_objetos = int(restricoes[0])
custo_maximo = int(restricoes[1])
custo_atual = custo_maximo

qtd_objetos_inseridos = 1

condicao_parada = True
obj_removido = False

objetos_inseridos = []
custos_inseridos = []
itens_inseridos = []
relacao_itens_sem_custo = []

while condicao_parada:
    acao_desejada = input()
    
    relacao_objeto = []

    if acao_desejada == acao4:
        print('Por nada! Estou sempre à disposição!')
        condicao_parada = False
    else:
        if acao_desejada == acao1:

            relacao_objeto = input()

            nome_objeto = relacao_objeto.split(' - ').pop(0)
            custo_objeto = int(relacao_objeto.split(' , ').pop(-1))

            if qtd_objetos_inseridos <= qtd_maxima_objetos and custo_objeto <= custo_atual: #É possível adicionar
                qtd_objetos_inseridos += 1 

                itens_inseridos.append(relacao_objeto)
                relacao_itens_sem_custo.append(relacao_objeto.split(' , '))
                objetos_inseridos.append(nome_objeto)
                custos_inseridos.append(custo_objeto)

                custo_atual -= custo_objeto
                
                print(f'Vá em frente, Ken! Você ainda tem {custo_atual} barbieCoins disponíveis')
            else:
                print('Avise a Barbie que isso não será possível.')


        if acao_desejada == acao2:
            objeto_remover = input()
            for obj in objetos_inseridos:
                if obj == objeto_remover: 
                    obj_removido = True

                    itens_inseridos.pop(objetos_inseridos.index(objeto_remover))
                    valor_removido = custos_inseridos.pop(objetos_inseridos.index(objeto_remover))
                    objetos_inseridos.remove(objeto_remover)
                    qtd_objetos_inseridos -= 1
                    custo_atual += valor_removido

                    print('Ok, Barbie!')
                    print(f'Ken, você ainda tem {custo_atual} barbieCoins disponíveis')
            
            if not obj_removido:
                print('Barbie, infelizmente não consegui fazer isso.')

        if acao_desejada == acao3:
            if itens_inseridos == []:
                print('Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!')
            else:
                print('Claro!')
                for relacao_item_splitado in relacao_itens_sem_custo:
                    for relacao_item_museu in relacao_item_splitado:
                        if relacao_item_splitado.index(relacao_item_museu) % 2 == 0:
                            print(relacao_item_museu)