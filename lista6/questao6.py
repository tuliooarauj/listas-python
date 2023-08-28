def converte_para_trigramas(linha, trigrama):
    if len(linha) < 3:
        return trigrama
    trigrama.append(linha[:3])
    return converte_para_trigramas(linha[1:], trigrama)

i = 0
linha_atual = ''
texto = {}

while linha_atual != 'end_of_file':
    linha_atual = input().lower()
    if not linha_atual == 'end_of_file':
        linha_atual_convertida = converte_para_trigramas(linha_atual, [])
        texto.update({i: linha_atual_convertida})
    i += 1

linhas_buscadas = {}
qtd_buscas = int(input())

for j in range(qtd_buscas):
    trecho_buscado = input().lower()
    trecho_buscado_convertido = converte_para_trigramas(trecho_buscado, [])
    linhas_buscadas.update({j: trecho_buscado_convertido})

linha_correspondente = []
for linha in linhas_buscadas.values():
    for trigrama in linha:
        for numero_linha, linhas_texto in texto.items():
            if trigrama in linhas_texto:
                linha_correspondente.append(numero_linha)

print(linha_correspondente[-1])