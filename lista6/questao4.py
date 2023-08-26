alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def cria_possibilidades(fake_string):
    for letra in alfabeto:
        palavra_formada = fake_string.replace('_', letra)
        palavras_formadas.append(palavra_formada)

def encontra_maior_repeticao(lista):
    maior = 0
    lista.sort()
    for palavra in lista:
        qtd_palavra = lista.count(palavra)
        if qtd_palavra > maior:
            maior = qtd_palavra
            palavra_repetida = palavra
 
    return palavra_repetida, maior

palavras_formadas = []

qtd_linhas = int(input())
for _ in range(qtd_linhas):
    fake_string = input()
    cria_possibilidades(fake_string)
resultado = encontra_maior_repeticao(palavras_formadas)

print(resultado[0], resultado[1])