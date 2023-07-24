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


x = eval('[[[1, 1], [3, 3], [5, 5]], [[6, 6], [8, 8]]]')

lista_distancias = []
posicao_explosao=[0, 0]
for i in x: #entrou na capsula
    for j in i: #entrou na coordenada
        distancia = ((int(posicao_explosao[0]) - int(j[0]))**2 + (int(posicao_explosao[1]) - int(j[1]))**2) ** (1/2)
        lista_distancias.append(distancia)