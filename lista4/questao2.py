def desclassificar_participante(idx_participante):
    lista_participantes.pop(idx_participante)

situacao = ''

situacao1 = 'Pit-Stop Espacial'
situacao2 = 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.'
situacao3 = 'Opa esse participante não está inscrito, desclassificando em 3, 2, 1...'

lista_participantes = []

while not situacao == 'FIM':
    
    informacoes_participante = input()
    lista_participantes.append(informacoes_participante)

    situacao = input()

    if situacao == situacao1:
