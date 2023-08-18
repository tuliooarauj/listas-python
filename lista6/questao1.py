relacao_famosos = {}

def retorna_string_invertida(string_qualquer):
    return string_qualquer[::-1]

def separa_mes(relacao_famoso, lista_numero):
    if relacao_famoso[:1] == ' ':
        if len(lista_numero) > 1:
            lista_numero = ''.join(lista_numero[::-1])
            return int(lista_numero), relacao_famoso[:0:-1]
        else:
            return int(lista_numero[0]), relacao_famoso[:0:-1]
    else:
        if relacao_famoso[:1].isnumeric():
            lista_numero.append(relacao_famoso[:1])
            relacao_famoso.replace(relacao_famoso[:1],'')
        return separa_mes(relacao_famoso[1:], lista_numero)


    
qtd_famosos = int(input())


for _ in range(qtd_famosos):
    access_key = []
    relacao_famoso = input()
    relacao = separa_mes(retorna_string_invertida(relacao_famoso), access_key)
    key_mes = relacao[0]
    nome_profissao = relacao[1]
    if key_mes in relacao_famosos:
        posicao_dic = len(relacao_famosos[key_mes]) + 1
        relacao_famosos[key_mes].update({posicao_dic : nome_profissao})
    else:
        posicao_dic = 1
        relacao_famosos[key_mes] = {posicao_dic : nome_profissao}

mes_consultado = int(input())

lista_fake = []

if mes_consultado in relacao_famosos:
    for famoso in relacao_famosos[mes_consultado].values():
        if 'fake' in famoso:
            lista_fake.append((famoso.replace(' fake','')))
    if lista_fake == []:
        print('Até agora não temos ninguém pra expor na internet neste mês :(')
    else:
        lista_fake.sort()
        print('Os fake nattys do mês são:')
        for famoso in lista_fake:
            print(famoso)
else:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
