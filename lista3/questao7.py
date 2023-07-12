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

cont = 0

condicao_parada = True
    
while condicao_parada:
    acao_desejada = input()

    if acao_desejada == 'Sair':
        condicao_parada = False
        print(itens_bolsa)
        if itens_bolsa == relacao_dia:
            print('Boa Barbie, foi na correria mas tudo deu certo!')
        else:
            for item_dia in relacao_dia:
                for item in itens_bolsa:
                    qtd_esquecido = 0
                    if not item_dia == item:
                        item_esquecido = item_dia
                        qtd_esquecido += 1
            if qtd_esquecido > 0:
                print(f'Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!')

            for item in itens_bolsa:
                for item_dia in relacao_dia:
                    itens_diferentes = 0
                    if not item == item_dia:
                        item_errado = item
                        itens_diferentes += 1
            if itens_diferentes > 0:
                print(f'Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_dia}')

    else:
        if acao_desejada == 'Adicionar':
            item_adicionado = False
            item_adicionar = input()
            for item_dia in relacao_dia:
                if item_dia == item_adicionar:
                    cont += 1
                    item_adicionado = True
                    print(f'{item_adicionar} adicionado à bolsa')
                    itens_bolsa.append(item_adicionar)

            if not item_adicionado:    
                print(f'Barbie, {item_adicionar} não esta na lista de itens de {profissao_dia}')
                
            if cont > 1:
                for item_bolsa in itens_bolsa:
                    if item_bolsa == item_adicionar:
                        print(f'Barbie, você já colocou {item_adicionar} na bolsa')
            
        if acao_desejada == 'Retirar':
            item_retirar = input()
            for item_bolsa in itens_bolsa:
                item_fora_bolsa = False
                if item_bolsa == item_retirar:
                    for item_dia in relacao_dia:
                        if item_dia == item_retirar:
                            item_a_usar = True #item que quer retirar está na bolsa, porém ele deve ser usado.
                        else: 
                            item_a_usar = False
                    if not item_a_usar:#item pode estar ou não estar na bolsa e ele não vai ser usado.
                        print(f'{item_retirar} retirado da bolsa')
                    if item_a_usar:
                        print(f'Não faca isso Barbie, você precisa de {item_retirar} para trabalhar de {profissao_dia}')
                else:
                    item_fora_bolsa = True
            if item_fora_bolsa and item_a_usar:          
                print('Barbie, como você vai retirar algo que já não esta ai?')