def converte_para_trigramas(linha, trigrama = None):
    if trigrama is None:
        trigrama = []

    if len(linha) == 3:
        return trigrama
    
    trigrama.append(linha[:3])
    return converte_para_trigramas(linha[1:], trigrama)

def testa_tam_string(string):
    if len(string) > 120:
        return string[:120]
    else:
        return string

i = 0
linha_atual = ''
texto = {}
texto_original = {}

while linha_atual != 'end_of_file':
    linha_atual = input().lower()
    #linha_atual = testa_tam_string(linha_atual)
    if not linha_atual == 'end_of_file':
        linha_atual_convertida = converte_para_trigramas(linha_atual)
        texto.update({i: linha_atual_convertida})
        texto_original.update({i: linha_atual})
    i += 1

linhas_buscadas = {}
linhas_buscadas_original = {}
qtd_buscas = int(input())

for j in range(qtd_buscas):
    trecho_buscado = input().lower()
    #trecho_buscado = testa_tam_string(trecho_buscado)
    trecho_buscado_convertido = converte_para_trigramas(trecho_buscado)
    linhas_buscadas.update({j: trecho_buscado_convertido})
    linhas_buscadas_original.update({j: trecho_buscado})

linha_correspondente = []
for linha in linhas_buscadas.values():
    trigrama = linha[0]
    for numero_linha, linhas_texto in texto.items():
        if trigrama in linhas_texto:
            linha_correspondente.append(numero_linha)
linha_correspondente = set(linha_correspondente)

linha_resultante = []
for trecho_buscado in linhas_buscadas_original.values():
    linha_contida = 0
    for linha in linha_correspondente:
        if trecho_buscado in texto_original[linha]:
            linha_contida += 1
            linha_resultante.append(linha)
    if linha_contida == 0:
        linha_resultante.append(-1)

for element in linha_resultante:
    print(element)