
posicao_x_estrela = int(input())
posicao_y_estrela = int(input())

matriz_valores = []

for linha in range(7):
    linha_matriz = []
    for coluna in range(7):
        linha_matriz.append('.')
    matriz_valores.append(linha_matriz)

matriz_valores[posicao_x_estrela][posicao_y_estrela] = '☆'

for matriz in matriz_valores:
    print(' '.join(matriz))

if matriz_valores[3][3] == '☆':
    print('Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!')
elif matriz_valores[0][posicao_y_estrela] == '☆' or matriz_valores[6][posicao_y_estrela] == '☆' or matriz_valores[posicao_x_estrela][0] == '☆' or matriz_valores[posicao_x_estrela][6] == '☆':
    print('Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...')
else:
    print('Ok, agora é só enviar a matriz!')

if matriz_valores[0][posicao_y_estrela] == '☆' or matriz_valores[6][posicao_y_estrela] == '☆' or matriz_valores[posicao_x_estrela][0] == '☆' or matriz_valores[posicao_x_estrela][6] == '☆':
    print('Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.')
else:
    print('Obrigado pela ajuda! A foto ficou ótima!')