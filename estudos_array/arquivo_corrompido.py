texto = 'O comando for & o t*pico de estudo deste projeto. Ele & #til para iterar sobre objetos iter@veis. Muitos problemas podem ser resolvidos com o aux!lio do comando for.'

#á foi trocado por @
#é foi trocado por &
#í foi trocado por !
#ó foi trocado por *
#ú foi trocado por #
print('\n\n\n\n')
print(f'Texto corrompido: {texto}')

for letra in '@&!*#':
    if letra == '@':
        texto = texto.replace('@','á')
    elif letra == '&':
        texto = texto.replace('&','é')
    elif letra == '!':
        texto = texto.replace('!','í')
    elif letra == '*':
        texto = texto.replace('*','ó')
    elif letra == '#':
        texto = texto.replace('#','ú')
print('\n\n')
print(f'Texto corrigido: {texto}')
print('\n\n\n\n')