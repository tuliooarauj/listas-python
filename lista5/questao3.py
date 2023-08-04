def encontra_suspeito(nome_buscado, string_buscada):
    if string_buscada == '':
      return False #Chegou no final da string e o suspeito não foi encontrado
    else:
      nome_analisado = string_buscada[:len(nome_buscado)]
      if nome_analisado == nome_buscado:
         return True
      else:
         return encontra_suspeito(nome_buscado, string_buscada[1:])

nome_suspeito = input()
string_concatenada = input()

if(encontra_suspeito(nome_suspeito.lower(), string_concatenada.lower())):
   print(f'Encontrei, o culpado é o {nome_suspeito}!')
else:
   print(f'Não era o {nome_suspeito}, tenho que continuar procurando.')