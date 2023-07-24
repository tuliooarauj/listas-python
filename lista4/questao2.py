def relatorio_participante(nome, qtd_propulsor, v_inicial, v_final):

    print(f'--- Participante: {nome} ---')
    print(f'Qtd de propulsores Final: {qtd_propulsor}')
    print(f'Velocidade Inicial: {v_inicial} km/h')
    print(f'Velocidade Final: {v_final} km/h')


situacao1 = 'Pit-Stop Espacial'
situacao2 = 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.'
situacao3 = 'Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...'


lista_participantes = []
idx = 0
corrida_finalizada = False
participante_desclassificado = 0
participante_removido = False

while not corrida_finalizada:
    situacao = ''

    if participante_removido:
        proxima_decisao = input() #proxima decisao pq pode estar se referenciando à situação ou dados do prox participante
        if proxima_decisao == 'FIM':
            corrida_finalizada = True
        else: #não está referenciando à fim, logo está referenciando aos dados do prox participante
            participante_removido = False
            informacoes_participante = proxima_decisao.split()
            lista_participantes.append(informacoes_participante)
            propulsor_participante = int(informacoes_participante[1])
    else: #caso padrão
        participante_removido = False
        informacoes_participante = input().split()
        lista_participantes.append(informacoes_participante)
        propulsor_participante = int(informacoes_participante[1])       

    while not situacao == 'Próximo' and not situacao == 'FIM' and not participante_removido: #condições que a rodada não acaba

        situacao = input()


        if situacao == situacao1:
            propulsor_participante += 1
        elif situacao == situacao2:
            propulsor_participante -= 1
            if propulsor_participante == 0:
                participante_desclassificado += 1
                print(f'BUUMM!! Infelizmente, {informacoes_participante[0]} está fora da corrida.')
                lista_participantes.remove(informacoes_participante)
                participante_removido = True

        elif situacao == situacao3:
            lista_participantes.remove(informacoes_participante)
            print(f'O {informacoes_participante[0]} achou que não descobriríamos, tirem {informacoes_participante[0]} imediatamente da pista.')
            participante_desclassificado += 1
            participante_removido = True

        elif situacao == 'FIM':
            corrida_finalizada = True

    if not participante_removido:
        if situacao == 'Próximo' or situacao == 'FIM':
            velocidade_inicial = int(informacoes_participante[1]) * int(informacoes_participante[2])
            velocidade_final = int(propulsor_participante) * int(informacoes_participante[2])

            relatorio_participante(informacoes_participante[0], propulsor_participante, velocidade_inicial, velocidade_final)
        
concluintes = (len(lista_participantes) + participante_desclassificado) - participante_desclassificado #total_participantes - desclassificados


if concluintes >= 1:
    print(f'Relatório da CIn Pod Race: {concluintes} participantes terminaram a corrida e {participante_desclassificado} foram desclassificados.')
else:
    print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')
