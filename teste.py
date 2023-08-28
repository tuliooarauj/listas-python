def cria_ns_fatoriais(numero):
    lista = []
    for fat in range(numero,-1,-1):
        lista.append(fat)
    return lista

print(cria_ns_fatoriais(5))