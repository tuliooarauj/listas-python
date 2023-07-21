def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def produto(a, b):
    return a * b
def divisao(a, b):
    return a / b
def potencia(a, b):
    return a ** b

string_soma = 'Quero somar esses dois números:'
string_subtracao = 'Preciso subtrair um pelo outro'
string_produto = 'Quanto dá o produto disso?'
string_divisao = 'Vou dividir aqui rapidinho'
string_potencia = 'E se eu elevar um pelo outro?'

qtd_operacoes = int(input())

for idx in range(1, qtd_operacoes + 1):
    operacao = input()
    operando1 = float(input())
    operando2 = float(input())
    
    if operacao == string_soma:
        resultado = soma(operando1, operando2)
        print(f'O resultado da {idx}ª operação foi {resultado:.2f}')
    elif operacao == string_subtracao:
        resultado = subtracao(operando1, operando2)
        print(f'O resultado da {idx}ª operação foi {resultado:.2f}')
    elif operacao == string_produto:
        resultado = produto(operando1, operando2)
        print(f'O resultado da {idx}ª operação foi {resultado:.2f}')
    elif operacao == string_divisao:
        resultado = divisao(operando1, operando2)
        print(f'O resultado da {idx}ª operação foi {resultado:.2f}')
    else:
        resultado = potencia(operando1, operando2)
        print(f'O resultado da {idx}ª operação foi {resultado:.2f}')

if not qtd_operacoes == 0:
    print('Ufa, já deu de cálculos por hoje!')
else:
    print('Vou relaxar aqui na minha nave')