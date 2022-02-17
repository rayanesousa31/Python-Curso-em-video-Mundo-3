#Crie um programa de 4 jogadores joguem um dado e
#tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário
#em ordem,sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ordem = list()

print('Valores sorteados:')
for j, r in jogo.items():
    print(f'{j} tirou {r} no dado')
    sleep(1)
ordem = sorted(jogo.items(), key = itemgetter(1),reverse = True)
print(ordem)
print('~~~~   RANKING DOS JOGADORES   ~~~~')
for i, r in enumerate(ordem):
    print(f'{i+1}º lugar: {r[0]} com {r[1]} pontos no dado')
    sleep(1)

