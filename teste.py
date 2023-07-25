def resolve_equacao_rpn(entrada):
    pilha = []
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in entrada.split():
        if token in operadores:
            # Se for um operador, desempilha os dois últimos operandos
            # e realiza a operação correspondente
            operando2 = pilha.pop()
            operando1 = pilha.pop()
            resultado = operadores[token](operando1, operando2)
            pilha.append(resultado)
        else:
            # Se for um operando, adiciona-o à pilha
            pilha.append(float(token))

    # O resultado final estará no topo da pilha
    return pilha[0]

# Exemplo de uso:
condicao = ''
soma = []
while condicao != 'oi':
    entrada = input()
    if not entrada == '':
        resultado = resolve_equacao_rpn(entrada)
        soma.append(resultado)
        somatorio = sum(soma)


print("Resultado:", soma)  # Deve imprimir 35.0
