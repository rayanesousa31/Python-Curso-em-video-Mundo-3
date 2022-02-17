#Aprimore o desafio 093 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))

    for c in range (0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper().strip() [0]
        if op in 'SN':
           break    
        print('ERRO! Responda apenas com S ou N.')
    if op == 'N':
        break
print('-='*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO Não existe jogador com o código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR -- {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print ('-' *30)

  