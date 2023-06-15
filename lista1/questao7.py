funcionalidadea = input()
funcionalidade_pontoa = int(input())

funcionalidadeb = input()
funcionalidade_pontob = int(input())

funcionalidadec = input()
funcionalidade_pontoc = int(input())

funcionalidaded = input()
funcionalidade_pontod = int(input())

funcionalidadee = input()
funcionalidade_pontoe = int(input())

funcionalidade1 = 'novo lançador de teias'
funcionalidade2 = 'lentes de visão avançada'
funcionalidade3 = 'traje à prova de balas'
funcionalidade4 = 'ativação de inteligência artificial'
funcionalidade5 = 'membranas planadoras'

soma_funcionalidades = funcionalidade_pontoa + funcionalidade_pontob + funcionalidade_pontoc + funcionalidade_pontod + funcionalidade_pontoe

if(funcionalidadea == 'NADA'):
    funcionalidade_pontoa = 0
elif(funcionalidadeb == 'NADA'):
    funcionalidade_pontob = 0
elif(funcionalidadec == 'NADA'):
    funcionalidade_pontoc = 0
elif(funcionalidaded == 'NADA'):
    funcionalidade_pontod = 0
elif(funcionalidadee == 'NADA'):
    funcionalidade_pontoe = 0

if(funcionalidadea == funcionalidade1):
    print('Com calma, aranha')
    if(funcionalidadeb == funcionalidade2):
        print('Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro')
        if(funcionalidadec == funcionalidade3):
            print('UOU, só tente sair dessa vivo, vou otimizar a energia aqui')
            
            
if(funcionalidadea == funcionalidade4) or (funcionalidadeb == funcionalidade4) or (funcionalidadec == funcionalidade4) or (funcionalidaded == funcionalidade4) or (funcionalidadee == funcionalidade4):
    print('Espero que não esteja ativando isso para usar nas provas') 


if(soma_funcionalidades >= 80):
    print('Vou descarregar em questão de minutos, pare AGORA')
    
contador = 0
    
if(funcionalidadea == funcionalidade1 or funcionalidadea == funcionalidade4 or funcionalidadea == funcionalidade5):
    contador+=1
if(funcionalidadeb == funcionalidade1 or funcionalidadeb == funcionalidade4 or funcionalidadeb == funcionalidade5):
    contador+=1
if(funcionalidadec == funcionalidade1 or funcionalidadec == funcionalidade4 or funcionalidadec == funcionalidade5):
    contador+=1
if(funcionalidaded == funcionalidade1 or funcionalidaded == funcionalidade4 or funcionalidaded == funcionalidade5):
    contador+=1
if(funcionalidadee == funcionalidade1 or funcionalidadee == funcionalidade4 or funcionalidadee == funcionalidade5):
    contador+=1
    
if(contador >= 3):
    print('Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa') 


    


print(f'Aranha, nessa sequência você usou {soma_funcionalidades} de energia!')

