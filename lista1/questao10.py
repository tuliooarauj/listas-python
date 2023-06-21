nome_aranha = input()
ataque_aranha = int(input())
defesa_aranha = int(input())
nome_aliado = input()
ataque_aliado = int(input())
defesa_aliado = int(input())

nome_vilao = input()
ataque_vilao = int(input())
defesa_vilao = int(input())
nome_capanga = input()
ataque_capanga = int(input())
defesa_capanga = int(input())

n = 1
ganhou_aranha = 0
ganhou_vilao = 0


print(f'{n}° confronto:')

fator_sorte_1 = int(input())

if(fator_sorte_1 == 0): #ambos atacam e defendem sozinhos
    if(ataque_aranha > defesa_vilao):
        ganhou_aranha+=1
        print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
    elif(ataque_aranha == defesa_vilao):
        ganhou_aranha+=1
        print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha pelo protagonismo
    else:
        ganhou_vilao+=1
        print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')  
else:
    if(fator_sorte_1 == 1): #o atacante ataca com seu parceiro
        ataque_aranha += ataque_aliado
        if(ataque_aranha > defesa_vilao):
            ganhou_aranha+=1
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
<<<<<<< HEAD
        elif(ataque_aranha == defesa_vilao):
            ganhou_aranha+=1
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha por atacar com o parceiro
        else:
            ganhou_vilao+=1
            print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')
=======
            ataque_aranha -= ataque_aliado
        elif(ataque_aranha == defesa_vilao):
            ganhou_aranha+=1
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha por atacar com o parceiro
            ataque_aranha -= ataque_aliado
        else:
            ganhou_vilao+=1
            print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')
            ataque_aranha -= ataque_aliado
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
    else:
        if(fator_sorte_1 == 2): # o defensor defende com seu parceiro
            defesa_vilao += defesa_capanga
            if(ataque_aranha > defesa_vilao):
                ganhou_aranha+=1
                print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
<<<<<<< HEAD
            elif(ataque_aranha == defesa_vilao):
                ganhou_vilao+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}') #o vilao ganha por defender com um parceiro
            else:
                ganhou_vilao+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')    
=======
                defesa_vilao -= defesa_capanga
            elif(ataque_aranha == defesa_vilao):
                ganhou_vilao+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}') #o vilao ganha por defender com um parceiro
                defesa_vilao -= defesa_capanga
            else:
                ganhou_vilao+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')    
                defesa_vilao -= defesa_capanga
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
        else:
            if(fator_sorte_1 == 3): #ambos atacam e defendem com seus respectivos parceiros       
                ataque_aranha += ataque_aliado
                defesa_vilao += defesa_capanga
                if(ataque_aranha > defesa_vilao):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
<<<<<<< HEAD
                elif(ataque_aranha == defesa_vilao):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha pelo protagonismo
                else:
                    ganhou_vilao+=1
                    print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')  
=======
                    ataque_aranha -= ataque_aliado
                    defesa_vilao -= defesa_capanga
                elif(ataque_aranha == defesa_vilao):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha pelo protagonismo
                    ataque_aranha -= ataque_aliado
                    defesa_vilao -= defesa_capanga
                else:
                    ganhou_vilao+=1
                    print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')
                    ataque_aranha -= ataque_aliado
                    defesa_vilao -= defesa_capanga  
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b


print(f'{n+1}° confronto:')
fator_sorte_2 = int(input())

if(fator_sorte_2 == 0): #ambos atacam e defendem sozinhos
    if(ataque_vilao > defesa_aranha):
        ganhou_vilao+=1
        print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}')
<<<<<<< HEAD
    elif(ataque_vilao == defesa_aranha):
        ganhou_aranha+=1
        print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha pelo protagonismo
    else:
        ganhou_aranha+=1
        print(f'O {nome_aranha} contra-atacou o {nome_vilao}')  
=======
        
    elif(ataque_vilao == defesa_aranha):
        ganhou_aranha+=1
        print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha pelo protagonismo
        
    else:
        ganhou_aranha+=1
        print(f'O {nome_aranha} contra-atacou o {nome_vilao}')  
        
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
else:
    if(fator_sorte_2 == 1): #o atacante ataca com seu parceiro
        ataque_vilao += ataque_capanga
        if(ataque_vilao > defesa_aranha):
            ganhou_vilao+=1
            print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}')
<<<<<<< HEAD
        elif(ataque_vilao == defesa_aranha):
            ganhou_vilao+=1
            print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}') #o vilao ganha por atacar com o parceiro
        else:
            ganhou_aranha+=1
            print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
=======
            ataque_vilao -= ataque_capanga
        elif(ataque_vilao == defesa_aranha):
            ganhou_vilao+=1
            print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}') #o vilao ganha por atacar com o parceiro
            ataque_vilao -= ataque_capanga
        else:
            ganhou_aranha+=1
            print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
            ataque_vilao -= ataque_capanga
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
    else:
        if(fator_sorte_2 == 2): # o defensor defende com seu parceiro
            defesa_aranha += defesa_aliado
            if(ataque_vilao > defesa_aranha):
                ganhou_vilao+=1
                print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}')
<<<<<<< HEAD
            elif(ataque_vilao == defesa_aranha):
                ganhou_aranha+=1
                print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha por defender com o parceiro
            else:
                ganhou_aranha+=1
                print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
=======
                defesa_aranha -= defesa_aliado
            elif(ataque_vilao == defesa_aranha):
                ganhou_aranha+=1
                print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha por defender com o parceiro
                defesa_aranha -= defesa_aliado
            else:
                ganhou_aranha+=1
                print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
                defesa_aranha -= defesa_aliado
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
        else:
            if(fator_sorte_2 == 3): #ambos atacam e defendem com seus respectivos parceiros       
                ataque_vilao += ataque_capanga
                defesa_aranha += defesa_aliado
                if(ataque_vilao > defesa_aranha):
                    ganhou_vilao+=1
                    print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}')
<<<<<<< HEAD
                elif(ataque_vilao == defesa_aranha):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha por protagonismo
                else:
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} contra-atacou o {nome_vilao}')

print(f'{n+2}° confronto:')
=======
                    ataque_vilao -= ataque_capanga
                    defesa_aranha -= defesa_aliado
                elif(ataque_vilao == defesa_aranha):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} contra-atacou o {nome_vilao}') #o aranha ganha por protagonismo
                    ataque_vilao -= ataque_capanga
                    defesa_aranha -= defesa_aliado
                else:
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
                    ataque_vilao -= ataque_capanga
                    defesa_aranha -= defesa_aliado

print(f'{n+2}° confronto:')

>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
fator_sorte_3 = int(input())

if(fator_sorte_3 == 0): #ambos atacam e defendem sozinhos
    if(ataque_aranha > defesa_vilao):
        ganhou_aranha+=1
        print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
    elif(ataque_aranha == defesa_vilao):
        ganhou_aranha+=1
        print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha pelo protagonismo
    else:
        ganhou_aranha+=1
        print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')  
else:
    if(fator_sorte_3 == 1): #o atacante ataca com seu parceiro
        ataque_aranha += ataque_aliado
        if(ataque_aranha > defesa_vilao):
            ganhou_aranha+=1
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
        elif(ataque_aranha == defesa_vilao):
            ganhou_aranha+=1
<<<<<<< HEAD
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha por atacar com o parceiro
=======
            print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha por atacar com parceiro
>>>>>>> 2762da149e443533c41500bd9029e2e03b40f00b
        else:
            ganhou_aranha+=1
            print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')
    else:
        if(fator_sorte_3 == 2): # o defensor defende com seu parceiro
            defesa_vilao += defesa_capanga
            if(ataque_aranha > defesa_vilao):
                ganhou_aranha+=1
                print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
            elif(ataque_aranha == defesa_vilao):
                ganhou_aranha+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}') #o vilao ganha por defender com um parceiro
            else:
                ganhou_aranha+=1
                print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')    
        else:
            if(fator_sorte_3 == 3): #ambos atacam e defendem com seus respectivos parceiros       
                ataque_aranha += ataque_aliado
                defesa_vilao += defesa_capanga
                if(ataque_aranha > defesa_vilao):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
                elif(ataque_aranha == defesa_vilao):
                    ganhou_aranha+=1
                    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}') #o aranha ganha pelo protagonismo
                else:
                    ganhou_aranha+=1
                    print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')  


if(ganhou_aranha >= 2):
    print(f'O {nome_aranha} e {nome_aliado} conseguiram derrotar o {nome_vilao} e recuperar o multiverso!')
else:
    print(f'O {nome_vilao} e {nome_capanga} invadiram Nova York, onde estão os outros aranhas??')