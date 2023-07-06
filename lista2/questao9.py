duracao_playlist = int(input())

meta_diaria = 10

nova_meta = 0


i = 0
while(i < 3):
    i+=1
    msc_mais_animada = ''
    indice_mais_animada = 0
    duracao_ultima_musica = 0

    print(f'Dia {i} do InterCIn')

    num_musicas_tocadas_dias = int(input())
    indice_ultima_musica = 0
    animacao_torcida = 0
    for j in range(num_musicas_tocadas_dias):
        nome_musica = input()
        duracao_musica_segundos = int(input())
        indice_animacao_musica = int(input())

        if(j==0):
            indice_ultima_musica = indice_animacao_musica
            duracao_ultima_musica = duracao_musica_segundos
        if(j!=0):
            indice_ultima_musica += indice_animacao_musica
            duracao_ultima_musica += duracao_musica_segundos

        if(i==1):
            consumo_playlist = duracao_playlist - duracao_ultima_musica
        if(i!=1):
            consumo_playlist = consumo_playlist - duracao_ultima_musica

        if(indice_animacao_musica > indice_mais_animada):
            indice_mais_animada = indice_animacao_musica
            msc_mais_animada = nome_musica
        
        animacao_torcida += int(indice_animacao_musica * 0.8)

    print(f'A música mais animada do dia foi {msc_mais_animada}')
  
    if(i==1):
        if(animacao_torcida < meta_diaria):
                nova_meta = 10 + (meta_diaria - animacao_torcida)
                print(f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {nova_meta} pontos de animação no outro dia')
        else:
            nova_meta = 10
        if(consumo_playlist <= 0):
            i = 10
    if(i==2):
        if(animacao_torcida < nova_meta): 
            nova_meta = 10 + (nova_meta - animacao_torcida)    
            print(f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {nova_meta} pontos de animação no outro dia')
        else:
            nova_meta = 10
        if(consumo_playlist <= 0):
            i = 10

    elif(i == 3): 

        if(consumo_playlist <= 0):
            i = 10
        else:
            if(animacao_torcida < nova_meta):
                print('Valeu a tentativa, na próxima vai dar bom')
                print('A playlist estava boa, mas não foi o suficiente para animar o evento')
            else:
                print('A playlist estava incrível demais!')

else:
    if(consumo_playlist <= 0):
        print('Estava animado, mas a playlist acabou antes do evento terminar e todo mundo ficou muito triste :(')




