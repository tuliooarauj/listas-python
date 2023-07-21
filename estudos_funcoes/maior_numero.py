def maior_numero(a, b):
    if a == b:
        print('Os números são iguais.')
    elif a > b:
        print(f'{a} é maior do que {b}.')
    else:
        print(f'{b} é maior do que {a}.')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

maior_numero(n1, n2)