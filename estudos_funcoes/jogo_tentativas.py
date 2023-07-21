from random import randint

def jogo_tentaticas():
    num = randint(0,100)
    acertou = False
    chute = int(input('Digite um número no intervalo de 0 a 100: '))
    num_tentativas = 0
    while not acertou:
        num_tentativas += 1
        if chute == num:
            print('Parabéns, vc acertou!')
            print(f'Número de tentativas: {num_tentativas}.')
            acertou = True
        elif chute > num:
            chute = int(input('Tente um número menor: '))
        else:
            chute = int(input('Tente um número maior: '))
    else:
        print('Fim de jogo!')


print('Vamos jogar um jogo de tentativas:')
jogo_tentaticas()
print('Vamos jogar novamente:')
jogo_tentaticas()