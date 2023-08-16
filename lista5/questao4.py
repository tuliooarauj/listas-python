def verifica_grau(string_grau_coeficiente, lista_grau_coeficiente, grau_polinomio):
    if len(lista_grau_coeficiente) < 1:
        caracter = string_grau_coeficiente[:len(grau_polinomio)]
        if caracter.isnumeric():
            lista_grau_coeficiente.append(int(caracter))
        return verifica_grau(string_grau_coeficiente[1:], lista_grau_coeficiente, grau_polinomio)
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
    if coeficiente == 0:
        return '0'
    elif coeficiente == 1:
        return 'x^'+str(grau)
    elif coeficiente == -1:
        return '-x^'+str(grau)
    elif grau == 0:
        return str(coeficiente)
    elif grau == 1:
        return str(coeficiente) + 'x'
    else:
        return str(coeficiente)+'x^'+str(grau)
    
def monta_derivada_monomio(monomio, coeficiente, grau, ordem):
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

def ordem_polinomio(polinomio):
    return polinomio.count('^')
def ordena_polinomio(polinomio):
    polinomio_FPB = sorted(polinomio, key=ordem_polinomio)
    return polinomio_FPB

grau_polinomio = input()
ordem_derivada = int(input())
coeficientes_nao_nulos = int(input())
monomios = []
derivadas = []

for _ in range(coeficientes_nao_nulos):
    grau_e_coeficiente = input()   
    grau = verifica_grau(grau_e_coeficiente, [], grau_polinomio)
    coeficiente = verifica_coeficiente(retorna_ultimos_4digitos(grau_e_coeficiente), [])
    monomio = monta_monomio(coeficiente, grau)
    derivada = monta_derivada_monomio(monomio, coeficiente, grau, ordem_derivada)
    monomios.append(monomio)
    if len(derivada) > 1:
        coeficiente = int(derivada[0])
        grau = int(derivada[1])
        monomio_derivado = monta_monomio(coeficiente, grau)
        derivadas.append(monomio_derivado)
    else:
        coeficiente = int(derivada)
        monomio_derivado = monta_monomio(coeficiente, grau)
        derivadas.append(monomio_derivado)

monomios_ordenados = ordena_polinomio(monomios)
polinomio = '+'.join(monomios_ordenados)
aparicoes_erradas = polinomio.count('+-')
polinomio_FPB = polinomio.replace('+-','-',aparicoes_erradas)
polinomio_derivadas = '+'.join(derivadas)

"""def remove_repetidos(string_repetida):
    if len(string_repetida) == 1:
        return string_repetida
    elif string_repetida[:1] != '0':
        return string_repetida
    else:
        if string_repetida[:1] == '0':
            return remove_repetidos(string_repetida[1:])"""

polinomio_FPB = polinomio_FPB.replace('0+','',polinomio_FPB.count('0'))
polinomio_derivadas_corrigido = polinomio_derivadas.replace('0+','',polinomio_derivadas.count('0'))   

print(f'A derivada {ordem_derivada} do polinômio {polinomio_FPB} é')
print(polinomio_derivadas_corrigido)

