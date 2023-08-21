def verifica_natty(categoria):
    if categoria == 'natty':
        return True
    return False

def ordena_maior_menor(dic_relacoes):
    relacao_ordenada = sorted(dic_relacoes, reverse=True)
    return relacao_ordenada

def ordena_dict(notas, dic_relacoes):
    for nota in notas:
        for key, element in dic_relacoes.items():
            if str(nota) in element:
                dic_relacoes[key] = dic_relacoes[notas.index(nota)]
                dic_relacoes[notas.index(nota)] = element
    return dic_relacoes

def main():
    i = 0
    j = 0
    nattys = {}
    notas_natty = {}
    fake_nattys = {}
    notas_fakenattys = {}
    qtd_string = int(input())

    for _ in range(qtd_string):
        relacao = input()
        nome, nota, categoria = relacao.split(' - ')
        if verifica_natty(categoria):
            nattys.update({i: relacao})
            notas_natty.update({i: int(nota)})
            i+=1 
        else:
            fake_nattys.update({j: relacao})
            notas_fakenattys.update({j: int(nota)})
            j+=1
        
    if not notas_natty == {}:
        notas_natty = ordena_maior_menor(notas_natty.values())
    if not notas_fakenattys == {}:
        notas_fakenattys = ordena_maior_menor(notas_fakenattys.values())
    
    nattys = ordena_dict(notas_natty, nattys)
    fake_nattys = ordena_dict(notas_fakenattys, fake_nattys)

    for natty in nattys.values():
        print(natty)
    for fakenatty in fake_nattys.values():
        print(fakenatty)
                
main()