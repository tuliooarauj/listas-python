def verifica_distintos(frase_ou_numero):
    resultado_lista = separa_algarismos_digitos(frase_ou_numero) 
    repetidos = len(resultado_lista)
    letras = 0
    for caracter in resultado_lista:
        if not repetidos < 1:
            caracter_repetido = resultado_lista.count(caracter)
            repetidos -= caracter_repetido
            letras += 1
    return letras