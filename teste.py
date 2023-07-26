# mensagem inicial
nome='Tantan'
print('Olá! '+ nome, end=". ")

# levantamento do volume de material
vol_mat = int(input())

#cálculo de cada casa
if(vol_mat>=0):
    cada_casa=int(vol_mat/3)
    print(nome+', voçê construiu '+ str(cada_casa)+ ' casa(s)')
else:
    print('Digite um valor válido e tente novamente')

#cálculo da sobra
sobra=vol_mat - cada_casa*3
print('E ainda sobrou '+ str(sobra) +' pack(s) de ferro para descarte.')