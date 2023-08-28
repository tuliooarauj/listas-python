def converte_para_trigramas(linha, trigrama):
    if len(linha) < 3:
        return trigrama
    trigrama.append(linha[:3])
    return converte_para_trigramas(linha[1:], trigrama)

i = 0
linha_atual = ''
texto = {}
texto_original = {}

while linha_atual != 'end_of_file':
    linha_atual = input().lower()
    if not linha_atual == 'end_of_file':
        linha_atual_convertida = converte_para_trigramas(linha_atual, [])
        texto.update({i: linha_atual_convertida})
        texto_original.update({i: linha_atual})
    i += 1

linhas_buscadas = {}
qtd_buscas = int(input())

for j in range(qtd_buscas):
    trecho_buscado = input().lower()
    trecho_buscado_convertido = converte_para_trigramas(trecho_buscado, [])
    linhas_buscadas.update({j: trecho_buscado_convertido})

linha_correspondente = []
for linha in linhas_buscadas.values():
    trigrama = linha[0]
    for numero_linha, linhas_texto in texto.items():
        if trigrama in linhas_texto:
            linha_correspondente.append(numero_linha)

linha_contida = 0
for linha in linha_correspondente:
    if trecho_buscado in texto_original[linha]:
        linha_contida += 1
        linha_resultante = linha
if linha_contida == len(linha_correspondente): #O trecho está contido em mais de uma linha
    print(linha_correspondente[0])
else:
    print(linha_resultante)