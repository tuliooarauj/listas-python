def encontrar_sobreviventes(raio, localizacoes_astronautas, local_explosao):
    lista_sobreviventes_capsula = []
    sobreviventes = 0
    for capsula in localizacoes_astronautas:
        lista_sobreviventes = []
        for astronauta in capsula:
            distancia = ((local_explosao[0] - astronauta[0])**2 + (local_explosao[1] - astronauta[1])**2 )**(1/2)
            if distancia > raio:
                lista_sobreviventes.append(astronauta)
                sobreviventes += 1
        lista_sobreviventes_capsula.append(lista_sobreviventes)
    return sobreviventes, lista_sobreviventes_capsula

def encontrar_pontocentral(raio, localizacoes_astronautas, local_explosao):
    
    media_geral = []

    posicao_sobreviventes = encontrar_sobreviventes(raio, localizacoes_astronautas, local_explosao)[1]
    for capsula in posicao_sobreviventes:
        somatorio_x = 0
        somatorio_y = 0
        qtd_astronauta = 0
        for astronauta in capsula:
            somatorio_x += astronauta[0]
            somatorio_y += astronauta[1]
            qtd_astronauta += 1
        if qtd_astronauta > 0:
            media_x = somatorio_x  / qtd_astronauta
            media_y = somatorio_y / qtd_astronauta
            media_capsula = [media_x, media_y]
            media_geral.append(media_capsula)
    
    
    return media_geral

    
def encontrar_astronautas(raio, localizacoes_astronautas, local_explosao):
    sobreviventes = encontrar_sobreviventes(raio, localizacoes_astronautas, local_explosao)[0]
    ponto_central = encontrar_pontocentral(raio, localizacoes_astronautas, local_explosao)
    relacao_encontrada = [sobreviventes, ponto_central]

    return relacao_encontrada

capsulas = eval(input())
posicao_explosao = eval(input())
raio_impacto = int(input())

print(encontrar_astronautas(raio_impacto, capsulas, posicao_explosao))
