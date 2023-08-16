def remover_ocorrencias(lista, valor):
    for elemento in lista[:]:  # Usamos lista[:] para criar uma cópia da lista original
        if elemento == valor:
            lista.remove(elemento)

# Exemplo de uso
minha_lista = [1, 2, 3, 2, 4, 2, 5]
valor_a_remover = 2
remover_ocorrencias(minha_lista, valor_a_remover)
print(minha_lista)  # A lista agora terá as ocorrências de 2 removidas
