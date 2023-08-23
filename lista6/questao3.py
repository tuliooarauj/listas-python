dialetos = {
    "Oooh look at him" : 0,
    "Baseball bat" : 1,
    "Aesthetic" : 2,
    "Fake Natty" : 3,
    "Chris Bumbstead, o CBUM" : 4,
    "Pope Francis" : 5,
    "O suco vicia" : 6,
    "I don't know you tell me" : 7,
    "Não é mesmo?" : 8,
    "Rodrigo Goes out" : 9}

def cria_fila():
    fila = {1: 0} #key = posicao fila, value = qtd_frente
    return fila

def verifica_possibilidade(qtd_frente, fila):
    if qtd_frente == len(fila):
        return True
    else:
        return False

def remove_zeros_esquerda(numero):
    if len(numero) > 1:
        if int(numero[:1]) != 0:
            return int(numero)
        else:
            return remove_zeros_esquerda(numero[1:])
    return int(numero)

def verifica_concatenacao(dialeto):
    if '+' in dialeto:
        return True
    else:
        return False

def cria_num_concatenacao(dialeto, dialetos): #string e dicionario
    lista_aux = []
    dialeto_concatenado = dialeto.split('+')
    for elemento in dialeto_concatenado:
        numero_equivalente = dialetos[elemento]
        lista_aux.append(str(numero_equivalente))
    numero_formado = ''.join(lista_aux)
    return numero_formado

possivel = True
qtd_pessoas = int(input())
for pessoas in range(qtd_pessoas):
    dialeto = input()
    if verifica_concatenacao(dialeto):
        numero = remove_zeros_esquerda(cria_num_concatenacao(dialeto, dialetos))
    else:
        numero = remove_zeros_esquerda(str(dialetos[dialeto]))

    if pessoas == 0 or numero == 0:
        fila = cria_fila()
    else:
        if verifica_possibilidade(dialetos[dialeto], fila):
            pos = len(fila)+1
            fila.update({pos: dialetos[dialeto]})
        else:
            possivel = False

if possivel:
    print('YES')
else:
    print('NO')