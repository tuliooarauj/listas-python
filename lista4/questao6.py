def res_notacao_polonesa(expressao):
    operador_soma = '+'
    operador_subtracao = '-'
    operador_produto = '*'
    operador_divisao = '/'

    operandos = []
    for elemento in expressao.split():
        if elemento == operador_soma: 
            soma = lambda a, b: a + b
            operando1 = operandos.pop() #vai retirar o último número adicionado à lista de operandos
            operando2 = operandos.pop() #vai retirar o penúltimo número adicionado à lista de operandos
            resultado = soma((operando2), (operando1))
            operandos.append(resultado)
        elif elemento == operador_subtracao:
            subtracao = lambda a, b: a - b
            operando1 = operandos.pop() #vai retirar o último número adicionado à lista de operandos
            operando2 = operandos.pop() #vai retirar o penúltimo número adicionado à lista de operandos
            resultado = subtracao((operando2), (operando1))
            operandos.append(resultado)
        elif elemento == operador_produto:
            produto = lambda a, b: a * b
            operando1 = operandos.pop() #vai retirar o último número adicionado à lista de operandos
            operando2 = operandos.pop() #vai retirar o penúltimo número adicionado à lista de operandos
            resultado = produto((operando2), (operando1))
            operandos.append(resultado)
        elif elemento == operador_divisao:
            divisao = lambda a, b: a / b
            operando1 = operandos.pop() #vai retirar o último número adicionado à lista de operandos
            operando2 = operandos.pop() #vai retirar o penúltimo número adicionado à lista de operandos
            resultado = divisao((operando2), (operando1))
            operandos.append(resultado)
        else:
            operandos.append(float(elemento))
            
    return (operandos[0])

def verificacao_nperfeito(numero):
    valor_analisado = int(res_notacao_polonesa(numero))
    lista_divisores = []
    for divisor in range(1, valor_analisado):
        if valor_analisado % divisor == 0:
            lista_divisores.append(divisor)
    somatorio = 0
    for divisor in lista_divisores:
        somatorio += divisor
    if not somatorio == 0:
        if somatorio == valor_analisado:
            return '1' #Numero perfeito
        else:
            return '0' #Numero não perfeito
    else:
        return '0' #Numero não perfeito
    
def consulta_tabela_ascii(somatorio_bloco):
    return chr(somatorio_bloco)

    
condicao = ''
resolucoes_bloco = []
palavra_formada = []

n = 0
while condicao != 'Todas as expressoes foram enviadas!':
    condicao = input()
    if not condicao == 'Todas as expressoes foram enviadas!':
        if not condicao == '':
            resolucoes_bloco.append(verificacao_nperfeito(condicao))
        else:
            n += 1
            binario = (''.join(resolucoes_bloco))
            conversao_inteiro =  int(binario, 2)
            palavra_formada.append((consulta_tabela_ascii(conversao_inteiro)))
            print(f'O {n}º conjunto de expressoes resultou no binario {binario} que em ASCII eh: {consulta_tabela_ascii(conversao_inteiro)}\n')
            resolucoes_bloco = []
    
print('A decodificacao final resultou em:')
print(''.join(palavra_formada))



