medica = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta' , 'Celular']
assistente_informatica = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
padeira = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
economista = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
personal_trainer = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']

itens_bolsa = []

profissao_prevista = input()
profissao_dia = input()

if profissao_prevista == 'Medica':
    relacao_prevista = medica
elif profissao_prevista  == 'Assistente de Informatica':
    relacao_prevista = assistente_informatica
elif profissao_prevista  == 'Padeira':
    relacao_prevista = padeira
elif profissao_prevista  == 'Economista':
    relacao_prevista = economista
elif profissao_prevista  == 'Personal Trainer':
    relacao_prevista = personal_trainer

if profissao_dia == 'Medica':
    relacao_dia = medica
elif profissao_dia  == 'Assistente de Informatica':
    relacao_dia = assistente_informatica
elif profissao_dia  == 'Padeira':
    relacao_dia = padeira
elif profissao_dia  == 'Economista':
    relacao_dia = economista
elif profissao_dia  == 'Personal Trainer':
    relacao_dia = personal_trainer

condicao_parada = True
    
while condicao_parada:
    acao_desejada = input()

    if acao_desejada == 'Sair':
        condicao_parada = False

    else:
        if acao_desejada == 'Adicionar':
            item_adicionado = False
            item = input()
            for item_dia in relacao_dia:
                if item_dia == item:
                    item_adicionado = True
                    print(f'{item} adicionado à bolsa')
                    itens_bolsa.append(item)

            if not item_adicionado:    
                print(f'Barbie, {item} não esta na lista de itens de {profissao_dia}')
                
            for item_bolsa in itens_bolsa:
                if item_bolsa == item:
                    print(f'Barbie, você já colocou {item} na bolsa')
            

