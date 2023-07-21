def relatorio_participante(nome, qtd_propulsor, v_inicial, v_final):

    print(f'--- Participante: {nome} ---')
    print(f'Qtd de propulsores Final: {qtd_propulsor}')
    print(f'Velocidade Inicial: {v_inicial} km/h')
    print(f'Velocidade Final: {v_final} km/h')

situacao = 'Próximo'

situacao1 = 'Pit-Stop Espacial'
situacao2 = 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.'
situacao3 = 'Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...'


lista_participantes = []
idx = 0
corrida_finalizada = False
participante_desclassificado = 0

while not corrida_finalizada:

    if situacao == 'Próximo':
        informacoes_participante = input().split()
        lista_participantes.append(informacoes_participante)
        idx += 1
        propulsor_participante = int(informacoes_participante[1])

    situacao = input()

    if situacao == 'Próximo' or situacao == 'FIM':
        velocidade_inicial = int(informacoes_participante[1]) * int(informacoes_participante[2])
        velocidade_final = int(propulsor_participante) * int(informacoes_participante[2])

        relatorio_participante(informacoes_participante[0], propulsor_participante, velocidade_inicial, velocidade_final)

    if situacao == situacao1:
        propulsor_participante += 1
    elif situacao == situacao2:
        propulsor_participante -= 1
        if propulsor_participante == 0:
            participante_desclassificado += 1
            print(f'BUUMM!! Infelizmente, {informacoes_participante[0]} está fora da corrida.')
            lista_participantes.remove(informacoes_participante)
            situacao = 'Próximo'
    elif situacao == situacao3:
        lista_participantes.remove(informacoes_participante)
        print(f'O {informacoes_participante[0]} achou que não descobriríamos, tirem {informacoes_participante[0]} imediatamente da pista.')
        participante_desclassificado += 1
        situacao = 'Próximo'

    elif situacao == 'FIM':
        corrida_finalizada = True

concluintes = (len(lista_participantes) + participante_desclassificado) - participante_desclassificado #total_participantes - desclassificados

if concluintes >= 1:
    print(f'Relatório da CIn Pod Race: {concluintes} participantes terminaram a corrida e {participante_desclassificado} foram desclassificados.')
else:
    print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')
