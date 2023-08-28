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

def cria_fila(num_fila):
    return {num_fila: []}


filas = []

nao_possivel = 0
lista_posicoes = {}
qtd_pessoas = int(input())

for pessoas in range(qtd_pessoas):
    dialeto = input()
    if verifica_concatenacao(dialeto):
        numero = int((cria_num_concatenacao(dialeto, dialetos)))
    else:
        numero = int((dialetos[dialeto]))
 
    sublistas = lista_posicoes.values()
    if numero in sublistas:
        i+=1
        nova_fila = []
        nova_fila.append(numero)
        lista_posicoes[i] = nova_fila
    else:
        i = 1
        filas.append(numero)
        lista_posicoes[i] = filas
    
    if verifica_possibilidade(lista_posicoes, numero) == False:
        nao_possivel += 1
   
if nao_possivel > 0:
    print('NO')
else:
    print('YES')