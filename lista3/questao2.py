lista_itens_deseja = []
lista_itens_deseja = input().split(', ')

lista_itens_possuidos = []
lista_itens_possuidos =  input().split(', ')

n_item = 0
ja_tem = False

for deseja in lista_itens_deseja:
    if lista_itens_possuidos.count(deseja):
        ja_tem = True    
        
if ja_tem:
    print('Esses são os itens que já tenho em casa:')
    for deseja in lista_itens_deseja:
        if lista_itens_possuidos.count(deseja):
            n_item+=1
            print(f'{n_item}º item: {deseja}')

if len(lista_itens_deseja) - n_item == len(lista_itens_deseja):
    print(f'Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(lista_itens_deseja)} itens em casa.')
elif len(lista_itens_deseja) - n_item > 0:
    print(f'Irei precisar comprar {len(lista_itens_deseja) - n_item} itens antes do meu encontro!')
else:
    print(f'Que ótimo, consegui encontrar cada um dos {n_item} itens!')
    
print('Isso é tudo! Hora de me preparar!')
                    
