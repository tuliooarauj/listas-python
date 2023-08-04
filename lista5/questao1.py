def sep_lower_upper(str_qualquer):
    minuscula = 0
    maiuscula = 0
    letras = []
    for letra in str_qualquer:
        letras.append(letra)
        if letra.islower():
            minuscula += 1
        else:
            maiuscula += 1
    tam_string = len(letras)
    return minuscula, maiuscula, tam_string

def calcula_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcula_fatorial(numero - 1)

def calcula_preco(str_qualquer):
    qtd_minuscula = sep_lower_upper(str_qualquer)[0]
    qtd_maiuscula = sep_lower_upper(str_qualquer)[1]
    tam = sep_lower_upper(str_qualquer)[2]
    if qtd_minuscula == qtd_maiuscula:
        return tam ** 2
    else:
        maior_aparicao = max(qtd_minuscula, qtd_maiuscula)
        return calcula_fatorial(maior_aparicao) * tam

grunhido = input()

preco = calcula_preco(grunhido)

if preco >= 100:
    print(f'Hum... {preco}? Acho que na volta eu compro')
else:
    print(f'{preco}! Vou comprar todos!')