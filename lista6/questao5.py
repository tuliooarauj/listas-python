goes_db = {}

def adicionar_suspeito(nome, banco_de_dados):
    banco_de_dados[nome] = {'Biceps': '', 'Treino': '','Frequencia': '', 'BF': '', 'Suor': ''}


def atualizar_suspeito(nome, caracteristicas, banco_de_dados):
    for caracteristica in caracteristicas.split(', '):
        elemento = caracteristica.split(': ')
        caracteristica_elemento = elemento.pop(0)
        valor = elemento[0]
        banco_de_dados[nome][caracteristica_elemento] = valor

def remover_suspeito(nome, banco_de_dados):
    del banco_de_dados[nome]

def converte_hora_seg_min(tempo):
    if 'hora' in tempo:
        valor = tempo.split()[0]
        valor = int(valor)
        return valor * 60 
    elif 'minuto' in tempo:
        valor = tempo.split()[0]
        valor = int(valor)
        return valor
    elif 'segundo' in tempo:
        valor = tempo.split()[0]
        valor = int(valor)
        return valor / 60
    
def remove_porcentagem(valor_com_porcentagem):
    return int(valor_com_porcentagem.replace('%',''))

def julgamento(nome, banco_de_dados):
    indicio_fakenatty = 0
    for caracteristica, valor in banco_de_dados[nome].items():
        if caracteristica == 'Biceps':
            if not valor == '':
                valor = valor.replace('cm','')
                if int(valor) > 45:
                    indicio_fakenatty += 1

        elif caracteristica == 'Treino':
            if not valor == '':
                valor = converte_hora_seg_min(valor)
                if valor < 30:
                    indicio_fakenatty += 1

        elif caracteristica == 'Frequencia':
            if not valor == '':
                valor = valor.replace('dias','')
                valor = valor.replace('dia','')
                if int(valor) < 4:
                    indicio_fakenatty += 1

        elif caracteristica == 'BF':
            if not valor == '':
                valor = remove_porcentagem(valor)
                if valor < 10:
                    indicio_fakenatty+=1

        elif caracteristica == 'Suor' and (valor == 'Seco' or valor == '') :
            indicio_fakenatty +=1

    if indicio_fakenatty >= 3:
        return True
    else:
        return False
    
def nattymeter(banco_de_dados):
    qtd_fakenatty = 0
    for nome in banco_de_dados.keys():
        if julgamento(nome, banco_de_dados):
            qtd_fakenatty += 1
    if qtd_fakenatty == 0:
        return None
    else:
        return qtd_fakenatty / len(banco_de_dados)*100
    
entrada = ''
while not entrada == 'FIM':
    entrada = input()

    if entrada == 'Adicionar suspeito':
        nome_suspeito = input()
        adicionar_suspeito(nome_suspeito, goes_db)
        print(f'Novo suspeito: {nome_suspeito}')

    elif entrada == 'Atualizar suspeito':
        nome_suspeito, caracteristicas = input().split('-> ')
        if not nome_suspeito in goes_db:
            print('Quem é esse crazy man? Não tá aqui na database')
        else: 
            atualizar_suspeito(nome_suspeito, caracteristicas, goes_db)

    elif entrada == 'Remover suspeito':
        nome_suspeito = input()
        if not nome_suspeito in goes_db:
            print('Quem é esse crazy man? Não tá aqui na database')
        else:
            remover_suspeito(nome_suspeito, goes_db)
            print(f'{nome_suspeito} removido da lista de suspeitos, está limpo')

    elif entrada == 'Julgamento':
        nome_suspeito = input()
        if not nome_suspeito in goes_db:
            print('Quem é esse crazy man? Não tá aqui na database')
        else:
            print(f'Eu já tenho o meu veredito, e o meu veredito, {nome_suspeito}:')
            if julgamento(nome_suspeito, goes_db):
                print('FAKE NATTY! USOU O SUCO!')
            else:
                print('Natural')

    elif entrada == 'NattyMeter':
        print('NattyMeter, ON!')
        resultado_nattymeter = nattymeter(goes_db)
        if resultado_nattymeter is None:
            print('Oh yeah, vivemos em uma sociedade sem suco, um great day')
        else:
            resultado_nattymeter = int(resultado_nattymeter)
            resultado_nattymeter = str(resultado_nattymeter)+'%'
            print(f'NOOO! {resultado_nattymeter} USARAM O SUCO')
