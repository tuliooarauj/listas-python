grau_polinomio = int(input())
ordem_derivada = int(input())
coeficientes_nao_nulos = int(input())
i = 0
polinomio = []
while i < coeficientes_nao_nulos:
    i+=1
    coeficiente_ordem = input()
    numeros = []  
    for caracter in coeficiente_ordem:
        if caracter.isnumeric():
            numeros.append(caracter)
    ordem_monomio = int(numeros[0])
    coeficiente_monomio = ''.join(numeros[1:])
    if int(coeficiente_monomio) > 0:
        if i == 1 and ordem_monomio > 1:
            monomio = coeficiente_monomio+'x^'+str(ordem_monomio)
        elif i == 1 and ordem_monomio == 1:
            monomio = coeficiente_monomio+'x'
        elif i ==1 and ordem_monomio == 0:
            monomio = coeficiente_monomio

        elif i > 1 and ordem_monomio > 1:
            monomio = '+'+coeficiente_monomio+'x^'+str(ordem_monomio)
        elif i > 1 and ordem_monomio == 1:
            monomio = '+'+coeficiente_monomio+'x'
        elif i > 1 and ordem_monomio == 0:
            monomio = '+'+coeficiente_monomio
    polinomio.append(monomio)

print(''.join(polinomio))