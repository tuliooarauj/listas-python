def calcular_fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

lista_fibo = []
for numero in range(0, 20):
    resultado_fibo = calcular_fibonacci(numero)
    lista_fibo.append(resultado_fibo)

condicao_inicial = input().split() #Nº de vidas e total de casas
qtd_vidas = int(condicao_inicial [0])
casas_passadas = 0

while casas_passadas < int(condicao_inicial[1]) and qtd_vidas > 0:
    numero_casa = int(input())
    if numero_casa in lista_fibo:
        casas_passadas += 1
    else:
        qtd_vidas -= 1
        casas_passadas = 0
        print('Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!')     
else:
    if qtd_vidas == 0:
        print('A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf')
    else:
        print('Voce Adicionou A Master Sword ao seu inventario')
        print('Link Salve Hyrule!!!')