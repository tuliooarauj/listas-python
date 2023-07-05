duracao_playlist = int(input())

meta_diaria = 10

nova_meta = 0

i = 0
while(i < 3):
    i+=1

    print(f'Dia {i} do InterCIn')

    num_musicas_tocadas_dias = int(input())

    for j in range(num_musicas_tocadas_dias):
        animacao_torcida = 0
        nome_musica = input()
        duracao_musica_segundos = int(input())
        indice_animacao_musica = int(input())

        if(j==0):
            indice_ultima_musica = 0
            indice_ultima_musica += indice_animacao_musica
            duracao_ultima_musica = 0
            duracao_ultima_musica += duracao_musica_segundos

        if(j>0):
            indice_ultima_musica = indice_animacao_musica
            indice_ultima_musica += indice_animacao_musica
            duracao_ultima_musica += duracao_musica_segundos

        if(i==1):
            consumo_playlist = duracao_playlist - duracao_ultima_musica
        if(i!=1):
            consumo_playlist = consumo_playlist - duracao_ultima_musica

        if(j == 0):
            indice_mais_animada = indice_animacao_musica
            msc_mais_animada = nome_musica

        if(indice_animacao_musica > indice_mais_animada):
            indice_mais_animada = indice_animacao_musica
            msc_mais_animada = nome_musica
        
    print(f'A música mais animada do dia foi {msc_mais_animada}')
  
    if(i==1 or i == 2):
        animacao_torcida += int(indice_ultima_musica * 0.8)
        if(animacao_torcida < meta_diaria):
            if(i==1):
                nova_meta = 10 + (meta_diaria - animacao_torcida )
                print(f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {nova_meta} pontos de animação no outro dia')
            elif(i==2):
                if(nova_meta == 0):
                    nova_meta = 10 + (meta_diaria - animacao_torcida )
                    print(f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {nova_meta} pontos de animação no outro dia')
                else:
                    nova_meta = 10 + (nova_meta - animacao_torcida)    
                    print(f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {nova_meta} pontos de animação no outro dia')
        if(consumo_playlist <= 0):
            i = 10
        else:
            meta_diaria = 10
    elif(i == 3):
        animacao_torcida += int(indice_ultima_musica * 0.8)

        if(animacao_torcida < meta_diaria):
            print('Valeu a tentativa, na próxima vai dar bom')
            print('A playlist estava boa, mas não foi o suficiente para animar o evento')
        else:
            print('A playlist estava incrível demais!')

else:
    if(consumo_playlist <= 0):
        print('Estava animado, mas a playlist acabou antes do evento terminar e todo mundo ficou muito triste :(')




