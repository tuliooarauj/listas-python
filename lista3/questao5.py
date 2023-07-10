n_andares_comodos = int(input())

for linha in range(n_andares_comodos):
    relacao_andares = []
    for coluna in range(n_andares_comodos):
        tamanho_comodo_andar = input()
        relacao_andares.append(tamanho_comodo_andar)
    print(' '.join(relacao_andares))