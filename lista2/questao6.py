n_integrantes = int(input())

termo_penultimo = 0
termo_ultimo = 1

if(n_integrantes > 0):
    print('A sequência de número das camisas do seu time será: ', end='')
    for i in range(1, n_integrantes):
        #f(0) = 0
        #f(1) = 1
        #f(n) = f(n-1) + f(n-2) p/ n >= 2

        #0-1-1-2-3-5-x = 5 + 3 ...
        #0-1-2-3-4
        
    #2(penultimo) + 3(ultimo) = 5(soma)
    #no prox: 5(soma) agora é peultimo e 3(ultimo) é penultimo

        soma = termo_ultimo + termo_penultimo 
        termo_ultimo = termo_penultimo 
        termo_penultimo = soma 

        print(str(soma)+', ' , end='')
    print(soma + termo_ultimo)
    
