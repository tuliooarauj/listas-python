duracao_playlist = int(input())

meta_diaria = 10
animacao_torcida = 0

i = 0
while(i <= 3):
    i+=1

    print(f'Dia {i} do InterCIn')

    num_musicas_tocadas_dias = int(input())
    nome_musica = input()
    duracao_musica_segundos = int(input())
    indice_animacao_musica = int(input())

    animacao_torcida += abs(indice_animacao_musica * 0.8)

    if(animacao_torcida < meta_diaria):
        nova_meta = 10 + (meta_diaria - animacao_torcida )
