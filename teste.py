x = []
y = [1, 2, 3, 4, 5]

if x == []:
    print('true')
else:
    print('false')

if y == []:
    print('true')
else:
    print('false')

    
for num in range(qtd_entradas_seguintes, -1, -1):
    if num == qtd_entradas_seguintes:
        fat = num - 0
    if num != qtd_entradas_seguintes:
        fat += num