vida_maxima_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())

vida_creeper = int(input())
ataque_creeper = ataque_venom

vida_atual_venom = vida_maxima_venom - ataque_creeper
vida_atual_creeper = vida_creeper - ataque_venom

tomou_pocao = 0
taxa_envenenamento = 0

inimigo1 = 'creeper'
inimigo2 = 'druida'

print(f'SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O {inimigo1.upper()}!')
if(vida_atual_venom <=0 and vida_atual_creeper <= 0): #caso especial dos dois morrerem
    personagem = 'venom'
    print(f'O {personagem} não tankou e foi de base...')
    print(f'O {inimigo1} não tankou e foi de base...')
    print('AH NÃO! O VENOM PEGOU EM BOMBA!')
    print('Pelo visto as aventuras do Miles terminaram por aqui...')
else:
    if(vida_atual_venom != 0 and vida_atual_creeper <= 0): #caso do creeper morrer (CRITERIO 1)
        personagem = inimigo1
        print(f'O {personagem} não tankou e foi de base...')
        print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
        if(vida_atual_venom + pocao_venom <= vida_maxima_venom):
            tomou_pocao = 1
            vida_atual_venom += pocao_venom
            print('Ah! Essa poção é da boa!')

        print(f'SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O {inimigo2.upper()}!') #TODOS OS CRITERIOS CASO A VITORIA SEJA PELA O CASO 1 DO CREEPER

        vida_druida = int(input())
        ataque_druida = int(input())

        vida_atual_druida = vida_druida - ataque_venom
    
        if(tomou_pocao == 0 or tomou_pocao == 1): 
            vida_atual_venom += pocao_venom 
            
            if(vida_atual_venom > vida_maxima_venom):
                taxa_envenenamento = vida_atual_venom - vida_maxima_venom
                vida_atual_venom -= taxa_envenenamento
                ataque_druida += taxa_envenenamento

            vida_atual_venom -= ataque_druida

            if(vida_atual_venom <= 0 and vida_atual_druida <= 0): #caso especial dos dois morrerem
                personagem = 'venom'
                print(f'O {personagem} não tankou e foi de base...')
                print(f'O {inimigo2} não tankou e foi de base...')
                print('Pelo visto a poção tava fora do prazo de validade :(')
                print('Pelo visto as aventuras do Miles terminaram por aqui...')
            else:
                if(vida_atual_venom != 0 and vida_atual_druida <= 0): #caso do druida morrer (CRITERIO 1)
                    personagem = inimigo2
                    print(f'O {personagem} não tankou e foi de base...')
                    print('Quase me dei mal, nunca mais aceito nada de estranho...')
                    print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                else:
                    if(vida_atual_venom <= 0 and vida_atual_druida != 0): #caso do venom morrer (CRITERIO 1)
                        personagem = 'venom'
                        print(f'O {personagem} não tankou e foi de base...')
                        print('Pelo visto a poção tava fora do prazo de validade :(')
                        print('Pelo visto as aventuras do Miles terminaram por aqui...')
                    else:
                        if(ataque_venom > ataque_druida): #caso do druida morrer (CRITERIO 2)
                            personagem = inimigo2
                            print(f'Vida atual do Venom: {vida_atual_venom}')
                            print(f'Dano sofrido pelo Venom: {ataque_druida }')
                            print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                            print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                            print('Quase me dei mal, nunca mais aceito nada de estranho...')
                            print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                        else:
                            if(ataque_druida > ataque_venom): #caso do venom morrer (CRITERIO 2)
                                personagem = 'venom'
                                print(f'Vida atual do Venom: {vida_atual_venom}')
                                print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                print('Pelo visto a poção tava fora do prazo de validade :(')
                                print('Pelo visto as aventuras do Miles terminaram por aqui...')
                            else:
                                if(vida_atual_druida < vida_atual_venom): #caso druida morrer (CRITERIO 3)
                                    personagem = inimigo2
                                    print(f'Vida atual do Venom: {vida_atual_venom}')
                                    print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                    print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                    print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                    print('Quase me dei mal, nunca mais aceito nada de estranho...')
                                    print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                                else:
                                    if(vida_atual_venom < vida_atual_druida): #caso venom morrer (CRITERIO 3)
                                        personagem = 'venom'
                                        print(f'Vida atual do Venom: {vida_atual_venom}')
                                        print(f'Dano sofrido pelo Venom: {ataque_druida }')
                                        print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                        print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                        print('Pelo visto a poção tava fora do prazo de validade :(')
                                        print('Pelo visto as aventuras do Miles terminaram por aqui...')
                                    else: #EMPATE (CRITERIO 4)
                                        
                                        print(f'Vida atual do Venom: {vida_atual_venom}')
                                        print(f'Dano sofrido pelo Venom: {ataque_druida }')
                                        print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                        print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                        print('Pelo visto a poção tava fora do prazo de validade :(')
                                        print('Pelo visto as aventuras do Miles terminaram por aqui...')


        else:
                
                    if(vida_atual_creeper < vida_atual_venom): #caso creeper morrer (CRITERIO 3)
                        personagem = inimigo1
                        print(f'Vida atual do Venom: {vida_atual_venom}')
                        print(f'Dano sofrido pelo Venom: {ataque_creeper}')
                        print(f'Vida atual do {inimigo1}: {vida_atual_creeper}')
                        print(f'Dano sofrido pelo {inimigo1}: {ataque_venom}')
                        print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
                        if(vida_atual_venom + pocao_venom <= vida_maxima_venom):
                            tomou_pocao = 1
                            vida_atual_venom += pocao_venom
                            print('Ah! Essa poção é da boa!')
                            
                        print(f'SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O {inimigo2.upper()}!') #TODOS OS CRITERIOS CASO A VITORIA SEJA PELA O CASO 3 DO CREEPER

                        vida_druida = int(input())
                        ataque_druida = int(input())

                        vida_atual_druida = vida_druida - ataque_venom
                        
                        if(tomou_pocao == 0 or tomou_pocao == 1):                          
                            vida_atual_venom += pocao_venom
                            if(vida_atual_venom > vida_maxima_venom):
                                taxa_envenenamento = vida_atual_venom - vida_maxima_venom
                                vida_atual_venom -= taxa_envenenamento
                                ataque_druida += taxa_envenenamento
                            if(vida_atual_venom <= 0 and vida_atual_druida <= 0): #caso especial dos dois morrerem
                                personagem = 'venom'
                                print(f'O {personagem} não tankou e foi de base...')
                                print(f'O {inimigo2} não tankou e foi de base...')
                                print('Pelo visto a poção tava fora do prazo de validade :(')
                                print('Pelo visto as aventuras do Miles terminaram por aqui...')
                            else:
                                if(vida_atual_venom != 0 and vida_atual_druida <= 0): #caso do druida morrer (CRITERIO 1)
                                    personagem = inimigo2
                                    print(f'O {personagem} não tankou e foi de base...')
                                    print('Quase me dei mal, nunca mais aceito nada de estranho...')
                                    print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                                else:
                                    if(vida_atual_venom <= 0 and vida_atual_druida != 0): #caso do venom morrer (CRITERIO 1)
                                        personagem = 'venom'
                                        print(f'O {personagem} não tankou e foi de base...')
                                        print('Pelo visto a poção tava fora do prazo de validade :(')
                                        print('Pelo visto as aventuras do Miles terminaram por aqui...')
                                    else:
                                        if(ataque_venom > ataque_druida): #caso do druida morrer (CRITERIO 2)
                                            personagem = inimigo2
                                            print(f'Vida atual do Venom: {vida_atual_venom}')
                                            print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                            print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                            print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                            print('Quase me dei mal, nunca mais aceito nada de estranho...')
                                            print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                                        else:
                                            if(ataque_druida > ataque_venom): #caso do venom morrer (CRITERIO 2)
                                                personagem = 'venom'
                                                print(f'Vida atual do Venom: {vida_atual_venom}')
                                                print(f'Dano sofrido pelo Venom: {ataque_druida }')
                                                print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                                print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                                print('Pelo visto a poção tava fora do prazo de validade :(')
                                                print('Pelo visto as aventuras do Miles terminaram por aqui...')
                                            else:
                                                if(vida_atual_druida < vida_atual_venom): #caso druida morrer (CRITERIO 3)
                                                    personagem = inimigo2
                                                    print(f'Vida atual do Venom: {vida_atual_venom}')
                                                    print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                                    print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                                    print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                                    print('Quase me dei mal, nunca mais aceito nada de estranho...')
                                                    print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
                                                else:
                                                    if(vida_atual_venom < vida_atual_druida): #caso venom morrer (CRITERIO 3)
                                                        personagem = 'venom'
                                                        print(f'Vida atual do Venom: {vida_atual_venom}')
                                                        print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                                        print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                                        print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                                        print('Pelo visto a poção tava fora do prazo de validade :(')
                                                        print('Pelo visto as aventuras do Miles terminaram por aqui...')
                                                    else: #EMPATE (CRITERIO 4)
                                                        
                                                        print(f'Vida atual do Venom: {vida_atual_venom}')
                                                        print(f'Dano sofrido pelo Venom: {ataque_druida}')
                                                        print(f'Vida atual do {inimigo2}: {vida_atual_druida}')
                                                        print(f'Dano sofrido pelo {inimigo2}: {ataque_venom}')
                                                        print('Pelo visto a poção tava fora do prazo de validade :(')
                                                        print('Pelo visto as aventuras do Miles terminaram por aqui...')

    else:
        if(vida_atual_venom < vida_atual_creeper): #caso venom morrer (CRITERIO 3)
            personagem = 'venom'
            print(f'Vida atual do Venom: {vida_atual_venom}')
            print(f'Dano sofrido pelo Venom: {ataque_creeper}')
            print(f'Vida atual do {inimigo1}: {vida_atual_creeper}')
            print(f'Dano sofrido pelo {inimigo1}: {ataque_venom}')
            print('AH NÃO! O VENOM PEGOU EM BOMBA!')
            print('Pelo visto as aventuras do Miles terminaram por aqui...')
        else: #EMPATE (CRITERIO 4)
            
            print(f'Vida atual do Venom: {vida_atual_venom}')
            print(f'Dano sofrido pelo Venom: {ataque_creeper}')
            print(f'Vida atual do {inimigo1}: {vida_atual_creeper}')
            print(f'Dano sofrido pelo {inimigo1}: {ataque_venom}')
            print('AH NÃO! O VENOM PEGOU EM BOMBA!')
            print('Pelo visto as aventuras do Miles terminaram por aqui...')
            








