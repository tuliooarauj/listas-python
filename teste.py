palavra = input().replace(' ', '').lower()



lista_digitos = []
for letra_ou_digito in palavra:
    lista_digitos.append(letra_ou_digito)
x = lista_digitos

letras = 0

resultado_lista = x
repetidos = len(resultado_lista)
for caracter in resultado_lista:
    if not repetidos < 1:
        caracter_repetido = resultado_lista.count(caracter)
        repetidos -= caracter_repetido
        letras += 1
    
print(letras) 

#9-2 = 7(1), 7-2 = 5(1), 5-2 = 3(1), 3-2 = 1 (1), 1-1 = 0(1)