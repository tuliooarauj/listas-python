def converte_para_trigramas(linha, trigrama = None):
    if trigrama is None:
        trigrama = []

    if len(linha) < 3:
        return trigrama
    
    trigrama.append(linha[:3])
    return converte_para_trigramas(linha[1:], trigrama)

print(converte_para_trigramas('Calegario e um otimo dancarino.'))