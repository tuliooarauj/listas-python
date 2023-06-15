dica = int(input())

if(dica % 2 == 0):
    dica = (dica / 2) ** 0.5 + 2
else:
    dica = (dica / 3) + 3

filme_procurado = dica

filme_1 = input()
filme_2 = input()
filme_3 = input()

cansaco = 0

if(filme_1 == 'Coringa' or filme_1 == 'Batman vs Superman' or filme_1 == 'O Cavaleiro das Trevas'): 
    print('Algo de errado não está certo!')
else:
    if(len(filme_1) != filme_procurado):
        print('Miles: Tou frio, melhor ir procurar nas fases mais antigas')
        cansaco += 1
        if(len(filme_2) != filme_procurado):
            print('Gwen: Cadê o velho??? Queria um autógrafo')
            cansaco += 1
            if(len(filme_3) != filme_procurado):
                print('Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...')
                cansaco += 1
            else:
                print('Miles: Achei o easter egg!!!')
                nome_filme = input()
                duracao = int(input())
                if(cansaco >= 2 and duracao >= 135):
                    print('Miles: A mimir')
                elif(cansaco >= 2) and (duracao >= 120 and duracao <= 135):
                    print('Gwen: Nada que uma xícara de café não resolva!')
                elif(cansaco < 2 or duracao < 120):
                    print(f'Peter: {nome_filme} é o melhor filme do homem aranha, 10/10')
        
                if(duracao == 180 ):
                    cansaco += 2
        else:
            print('Miles: Achei o easter egg!!!')
            nome_filme = input()
            duracao = int(input())
            if(cansaco >= 2 and duracao >= 135):
                print('Miles: A mimir')
            elif(cansaco >= 2) and (duracao >= 120 and duracao <= 135):
                print('Gwen: Nada que uma xícara de café não resolva!')
            elif(cansaco < 2 or duracao < 120):
                print(f'Peter: {nome_filme} é o melhor filme do homem aranha, 10/10')
            
            if(duracao == 180 ):
                cansaco += 2
    else:
        print('Miles: Achei o easter egg!!!')
        nome_filme = input()
        duracao = int(input())
        if(cansaco >= 2 and duracao >= 135):
            print('Miles: A mimir')
        elif(cansaco >= 2) and (duracao >= 120 and duracao <= 135):
            print('Gwen: Nada que uma xícara de café não resolva!')
        elif(cansaco < 2 or duracao < 120):
            print(f'Peter: {nome_filme} é o melhor filme do homem aranha, 10/10')
            
        if(duracao == 180 ):
            cansaco += 2

        

    



