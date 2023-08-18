relacao_famosos = {}

def find_fakenatty(string_famoso):
    if 'fake' in  string_famoso:
        return True
    else:
        return False
    
def remove_repetidos(relacao_famosos, nome):

    for key, value in relacao_famosos.items():
        for key1, value1 in value.items():
            if value1 == nome:
                del relacao_famosos[key][key1]
                return relacao_famosos
    return False
  
qtd_famosos = int(input())

for _ in range(qtd_famosos):
    nome, resto_string = input().split(' - ')
    profissao, veredito, mes = resto_string.split(' ')
    mes = int(mes)
    remove_repetidos(relacao_famosos, nome +' - '+ profissao + veredito)
    if mes in relacao_famosos:
        posicao_dic = len(relacao_famosos[mes]) + 1
        relacao_famosos[mes].update({posicao_dic : nome +' - '+ profissao + veredito})
    else:
        posicao_dic = 1
        relacao_famosos[mes] = {posicao_dic : nome +' - '+ profissao + veredito}

mes_consultado = int(input())

lista_fake = []




if mes_consultado in relacao_famosos:
    for famoso in relacao_famosos[mes_consultado].values():
        if find_fakenatty(famoso):
            lista_fake.append((famoso.replace('fake','')))
    if lista_fake == []:
        print('Até agora não temos ninguém pra expor na internet neste mês :(')
    else:
        lista_fake.sort()
        print('Os fake nattys do mês são:')
        for famoso in lista_fake:
            print(famoso)
else:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
