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


def verifica_possibilidade(qtd_frente, fila):
    if qtd_frente == len(fila):
        return True
    else:
        return False

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

def cria_n_fatoriais(numero):
    lista = []
    for fat in range(numero,-1,-1):
        lista.append(fat)
    return lista

def verifica_possibilidade(lista_posicoes, numero):
    fatorial_n = cria_n_fatoriais(numero)
    for elemento in fatorial_n:
        if elemento in lista_posicoes:
            fatorial_presente = True
        else:
            return False
    if fatorial_presente:
        return True

def verifica_numero_existe(numero, dicionario):
    for num_fila, fila in dicionario.items():
        if not numero in fila:
            return False, num_fila
    return True, num_fila


filas = []

nao_possivel = 0
qtd_pessoas = int(input())
num_fila = 1
lista_posicoes = {}
lista_posicoes[num_fila] = []

for pessoas in range(qtd_pessoas):
    dialeto = input()
    if verifica_concatenacao(dialeto):
        numero = int((cria_num_concatenacao(dialeto, dialetos)))
    else:
        numero = int((dialetos[dialeto]))

    resultado = verifica_numero_existe(numero, lista_posicoes)
    

    if resultado[0]:
        num_fila += 1
        lista_posicoes[num_fila] = []
        lista_posicoes[num_fila].append(numero)
        if verifica_possibilidade(lista_posicoes[num_fila], numero) == False:
            nao_possivel += 1
    else:
        posicao_fila = resultado[1]
        lista_posicoes[posicao_fila].append(numero)
        if verifica_possibilidade(lista_posicoes[posicao_fila], numero) == False:
            nao_possivel += 1
         
    
   
if nao_possivel > 0:
    print('NO')
else:
    print('YES')