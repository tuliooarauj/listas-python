palavra = input()

lista_digitos = []
for letra_ou_digito in palavra:
    lista_digitos.append(letra_ou_digito)

lista_digitos_inversa = lista_digitos[::-1] #slicing reverso
                       
if lista_digitos == lista_digitos_inversa:
    print('palindromo') #É palíndromo
else:
    print('nao palindromo') #Não é palíndromo

