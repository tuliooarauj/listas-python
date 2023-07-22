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
    n_distintos = len(set(resultado_lista)) #metodo set retorna os digitos únicos
    return n_distintos   

n_frases = int(input())

for i in range(n_frases):
    string_analisada = input()
    string_modificada = string_analisada.lower().replace(' ','')
    if verifica_palindromo(string_modificada):
        if string_analisada.isnumeric():
            print(f'O número "{string_analisada}" é um palíndromo!')
            qtd_distintos = verifica_distintos(string_modificada)
            print(f'Há {qtd_distintos} número(s) distinto(s) na sequência de números.')
        else:
            print(f'A frase "{string_analisada}" é um palíndromo!')
            qtd_distintos = verifica_distintos(string_modificada)
            print(f'Há {qtd_distintos} letra(s) distinta(s) na frase.')
    else:
        print('A frase ou o número não é um palíndromo.')
