goes_db = {}
caracteristicas_gerais = {'Biceps': '', 'Treino': '','Frequencia': '', 'BF': '', 'Suor': ''}

def adicionar_suspeito(nome, banco_de_dados):
    banco_de_dados.update({nome: caracteristicas_gerais})

def atualizar_suspeito(nome, caracteristicas, banco_de_dados):
    for caracteristica in caracteristicas.split(', '):
        elemento = caracteristica.split(': ')
        caracteristica_elemento = elemento.pop(0)
        valor = elemento[0]
        banco_de_dados[nome].update({caracteristica_elemento: valor})

def remover_suspeito(nome, banco_de_dados):
    del banco_de_dados[nome]

def converte_hora_seg_min(tempo):
    if 'hora' in tempo:
        valor = tempo.split()[0]
        valor = int(valor)
        return valor * 60 
    elif 'minuto' in tempo:
        valor = tempo.split()[0]
        return valor
    elif 'segundo' in tempo:
        valor = tempo.split()[0]
        return valor / 60
    
def remove_porcentagem(valor_com_porcentagem):
   return int(valor_com_porcentagem.replace('%',''))

def julgamento(nome, banco_de_dados):
    indicio_fakenatty = 0
    for caracteristica, valor in banco_de_dados[nome].items():
        if caracteristica == 'Biceps' and int(valor) > 45:
            indicio_fakenatty += 1
        elif caracteristica == 'Treino':
            valor = converte_hora_seg_min(valor)
            if valor < 30:
                indicio_fakenatty += 1
        elif caracteristica == 'Frequencia' and int(valor) < 4:
            indicio_fakenatty += 1
        elif caracteristica == 'BF':
            valor = remove_porcentagem(valor)
            if valor < 10:
                indicio_fakenatty+=1
        elif caracteristica == 'Suor' and (valor == 'Seco' or valor == ''):
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
        return qtd_fakenatty / len(banco_de_dados)+'%'



print(goes_db)