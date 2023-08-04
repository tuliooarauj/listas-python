def checagem_palindromo():
    lista_palindromo = []

    for caractere in sentenca_modificada:

        lista_palindromo.append(caractere)

    lista_reversa = lista_palindromo[::-1]

    if sentenca_modificada in lista_sequencia_frases:

        if sentenca_modificada == lista_reversa:
            print(f'A frase "{sentenca}" é um palíndromo!')

        else:
            print('A frase ou o número não é um palíndromo.')

    elif int(sentenca_modificada) in lista_sequencia_numeros:

        if sentenca_modificada == lista_reversa:
            print(f'O número "{sentenca}" é um palíndromo!')

        else:
            print('A frase ou o número não é um palíndromo.')

def contagem_caractere():
    if sentenca_modificada in lista_sequencia_frases:
        contagem_letras = 0

        for caractere in sentenca:

            if caractere in alfabeto:
                contagem_letras += 1
                alfabeto.pop(caractere)

        print(f'Há {contagem_letras} letra(s) distinta(s) na frase.')

    elif sentenca_modificada in lista_sequencia_numeros:
        contagem_numeros = 0

        for caractere in algarismo:
            contagem_numeros += 1
            algarismo.pop(caractere)

        print(f'Há {contagem_numeros} número(s) distinto(s) na sequência de números.')

numero_sentenca = int(input())

palindromo_existe = 0

lista_sequencia_numeros = []

lista_sequencia_frases = []

algarismo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for sentenca in range(numero_sentenca):

    sentenca = input()
    sentenca_modificada = sentenca.lower().replace(' ','')
    checagem = list(sentenca_modificada)
    amostra = checagem[0]

    if amostra.isnumeric():
        lista_sequencia_numeros.append(int(sentenca_modificada))
        checagem_palindromo()
        
    
    else:
        lista_sequencia_frases.append(sentenca_modificada)
        checagem_palindromo()





