def separa_algarismos_digitos(string_qualquer):
    lista_digitos = []
    for letra_ou_digito in string_qualquer:
        lista_digitos.append(letra_ou_digito)
    return lista_digitos

def verifica_palindromo(frase_ou_numero):
    resultado_lista = separa_algarismos_digitos(frase_ou_numero)
    resultado_lista_invertida = resultado_lista[::-1]
    if resultado_lista == resultado_lista_invertida:
        return True #É palíndromo
    else:
        return False #Não é palíndromo

def verifica_distintos(frase_ou_numero):
    resultado_lista = separa_algarismos_digitos(frase_ou_numero)
    for caracter in resultado_lista:
        caracter_repetido = resultado_lista.count(caracter)
        x = len(resultado_lista) - caracter
