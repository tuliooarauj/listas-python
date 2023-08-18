def verifica_grau(string_grau_coeficiente, lista_grau_coeficiente, grau_polinomio):
    if not string_grau_coeficiente[:1] == ' ':
        caracter = string_grau_coeficiente[:1]
        if caracter.isnumeric():
            lista_grau_coeficiente.append(int(caracter))
        return verifica_grau(string_grau_coeficiente[1:], lista_grau_coeficiente, grau_polinomio)
    else:
        if len(lista_grau_coeficiente) > 1:
            string_lista = [str(numero) for numero in lista_grau_coeficiente]
            string_numeros_formados = ''.join(string_lista)
            return int(string_numeros_formados)
        else:
            return lista_grau_coeficiente[0]

def retorna_ultimos_4digitos(string_grau_coeficiente):
    return string_grau_coeficiente[:-5:-1] #coeficiente varia de (-1000, 1000)
    
def verifica_coeficiente(string_grau_coeficiente_modificada, lista_coeficiente):
    caracter_lista = string_grau_coeficiente_modificada[:1]
    if string_grau_coeficiente_modificada == '':
        coeficiente = ''.join(lista_coeficiente[::-1])
        return int(coeficiente)
    else:
        if caracter_lista.isnumeric() or caracter_lista == '-':
            lista_coeficiente.append(caracter_lista)
        return verifica_coeficiente(string_grau_coeficiente_modificada[1:], lista_coeficiente)
    

        
def monta_monomio(coeficiente, grau):
    if coeficiente == []:
        coeficiente = 0
    if coeficiente == 0:
        return '0'
    elif grau == 0:
        return str(coeficiente)
    elif coeficiente == 1:
        return 'x^'+str(grau)
    elif coeficiente == -1:
        return '-x^'+str(grau)
    elif grau == 1:
        return str(coeficiente) + 'x'
    else:
        return str(coeficiente)+'x^'+str(grau)
    
def monta_derivada_monomio(monomio, coeficiente, grau, ordem):
    if coeficiente == []:
        coeficiente = 0
    if monomio == str(coeficiente):
        return '0'
    elif monomio == str(coeficiente)+'x':
        resultado = str(coeficiente), str(grau - 1)
        if ordem == 1:
            return resultado
        else:
            monomio = monta_monomio(int(resultado[0]), int(resultado[1]))
            return monta_derivada_monomio(monomio, int(resultado[0]), int(resultado[1]), ordem - 1)
    else:
        resultado = str(grau * coeficiente), str(grau - 1)
        if ordem == 1:
            return resultado
        else:
            monomio = monta_monomio(int(resultado[0]), int(resultado[1]))
            return monta_derivada_monomio(monomio, int(resultado[0]), int(resultado[1]), ordem - 1)

def cria_lista_coeficientes(lista_polinomio, grau_polinomio):
    for _ in range(int(grau_polinomio)+1):
        lista_polinomio.append([])
    return lista_polinomio

def ordena_coeficientes_polinomio(coeficiente, grau, lista_polinomio):
    lista_polinomio[grau] = coeficiente
    return lista_polinomio

grau_polinomio = input()
ordem_derivada = int(input())
coeficientes_nao_nulos = int(input())
monomios = []
derivadas = []

coeficientes_ordenados = cria_lista_coeficientes([], grau_polinomio)

for _ in range(coeficientes_nao_nulos):

    grau_e_coeficiente = input()   
    grau = verifica_grau(grau_e_coeficiente[15:], [], grau_polinomio)
    coeficiente = verifica_coeficiente(retorna_ultimos_4digitos(grau_e_coeficiente), [])
    ordena_coeficientes_polinomio(coeficiente, int(grau), coeficientes_ordenados)

i = 0
for coeficiente in coeficientes_ordenados:
    
    monomio = monta_monomio(coeficiente, coeficientes_ordenados.index(coeficiente))
    monomios.append(monomio)
    derivada = monta_derivada_monomio(monomio, coeficiente, coeficientes_ordenados.index(coeficiente), ordem_derivada)

    if len(derivada) > 1:
        coeficiente = int(derivada[0])
        grau = int(derivada[1])
        monomio_derivado = monta_monomio(coeficiente, grau)
        derivadas.append(monomio_derivado)
        coeficientes_ordenados[i] = []
    else:
        coeficiente = int(derivada)
        monomio_derivado = monta_monomio(coeficiente, grau)
        derivadas.append(monomio_derivado)
        coeficientes_ordenados[i] = []
    i+=1

if len(monomios) > 1:
    for elemento in monomios[:]:
        if elemento == '0' or elemento == '[]':
            monomios.remove(elemento)
    if monomios == []:
        monomios.append('0')
if len(derivadas) > 1:
    for elemento in derivadas[:]:
        if elemento == '0':
            derivadas.remove(elemento)
    if derivadas == []:
        derivadas.append('0')


polinomio = '+'.join(monomios)
aparicoes_erradas_polinomio = polinomio.count('+-')
polinomio_FPB = polinomio.replace('+-','-',aparicoes_erradas_polinomio)

polinomio_derivado = '+'.join(derivadas)
aparicoes_erradas_derivadas = polinomio_derivado.count('+-')
polinomio_derivado_FPB = polinomio_derivado.replace('+-','-',aparicoes_erradas_derivadas)

if ordem_derivada == 0:
    polinomio_derivado_FPB = polinomio_FPB


print(f'A derivada {ordem_derivada} do polinômio {polinomio_FPB} é')
print(polinomio_derivado_FPB)

