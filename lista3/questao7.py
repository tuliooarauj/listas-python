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

itens_bolsa = relacao_prevista

condicao_parada = True
    
while condicao_parada:
    acao_desejada = input()

    if acao_desejada == 'Sair':
        condicao_parada = False
        itens_bolsa_sorted = sorted(itens_bolsa)
        relacao_dia_sorted = sorted(relacao_dia)
        print('Itens na bolsa: ', end='')
        print(', '.join(itens_bolsa_sorted))
        if itens_bolsa_sorted == relacao_dia_sorted:
            print('Boa Barbie, foi na correria mas tudo deu certo!')
        else:
            for item_dia in relacao_dia: #possivel erro
                for item in itens_bolsa:
                    qtd_esquecido = 0
                    if not item_dia == item:
                        item_esquecido = item_dia
                        qtd_esquecido += 1
            if qtd_esquecido > 0:
                print(f'Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!')

            for item in itens_bolsa:
                contador_itens_diferentes = 0
                for item_dia in relacao_dia:
                    if not item == item_dia:
                        contador_itens_diferentes += 1
                        if contador_itens_diferentes == len(relacao_dia):
                            item_errado = item
                            print(f'Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_dia}')           

    else:
        if acao_desejada == 'Adicionar':
            item_adicionado = False
            item_adicionar = input()

            for item_bolsa in itens_bolsa:
                if item_bolsa == item_adicionar:
                    print(f'Barbie, você já colocou {item_adicionar} na bolsa')
                    item_adicionado = True
                
            if not item_adicionado:
                for item_dia in relacao_dia:
                    if item_dia == item_adicionar:
                        item_adicionado = True
                        print(f'{item_adicionar} adicionado à bolsa')
                        itens_bolsa.append(item_adicionar)

            if not item_adicionado:    
                print(f'Barbie, {item_adicionar} não esta na lista de itens de {profissao_dia}')
                          
            
        if acao_desejada == 'Retirar':
            item_a_retirar = input()
            item_fora_bolsa = 0
            item_nfaz_parte_profissao = 0
            for item_bolsa in itens_bolsa:
                if not item_a_retirar == item_bolsa: #testando se o item a retirar não está na bolsa
                    item_fora_bolsa +=1 
                else: #o item está na bolsa
                    for item_dia in relacao_dia:
                        if item_a_retirar == item_dia: #testando se o item a retirar faz parte da profissão do dia
                            print(f'Não faca isso Barbie, você precisa de {item_a_retirar} para trabalhar de {profissao_dia}')
                        else:
                            item_nfaz_parte_profissao += 1
                    if item_nfaz_parte_profissao == len(relacao_dia):
                        print(f'{item_a_retirar} retirado da bolsa')
                        itens_bolsa.remove(item_a_retirar)
                    
                if item_fora_bolsa == len(itens_bolsa):
                    print('Barbie, como você vai retirar algo que já não esta ai?')




