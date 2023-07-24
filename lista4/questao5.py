def vogal_ou_consoante(string_analisada):
    qtd_vogal = 0
    qtd_consoante = 0
    string_analisada = string_analisada.lower()
    for caracter in string_analisada:
        if not caracter.isnumeric():
            if caracter in 'aeiou':
                qtd_vogal += 1
            else:
                qtd_consoante += 1
    return qtd_vogal, qtd_consoante

def eh_multiplo(string_analisada):
    lista_caracteres = []
    nao_multiplo = 0
    for caracter in string_analisada:
        if caracter.isnumeric():
            lista_caracteres.append(caracter)
    for numero in lista_caracteres:
        if not numero % lista_caracteres[0] == 0: # encontrar pelo menos um que não é divisível
            nao_multiplo += 1
        
    if nao_multiplo == 0:
        return True #eh multiplo e a posição vale 3
    else:
        return False
        


def decodificar_codigo(string):
    if not eh_multiplo(string):
        qtd_vogal = vogal_ou_consoante(string)[0]
        qtd_consoante = vogal_ou_consoante(string)[1]

        if qtd_consoante == 0:
            coordenada_posicao = 0
        else:
            passo2 = qtd_vogal / qtd_consoante
            passo3 = int(passo2) #aplicando a func. piso no passo 3
            passo4 = passo3 % 7
            coordenada_posicao = passo4
    return coordenada_posicao
        
    


    
#print(vogal_ou_consoante('uuuu2apAeIoUBeOoUauEeAa7iOuaa'))