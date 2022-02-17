#Faça um programa que tenha uma função chamada  contador(), que receba
#três parâmetros: início, fim e passo e  realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#- De 1 ate 10, de 1 em 1
#- De 10 até 0, de 2 em 2
#- Uma contagem personalizada
from time import sleep

import time
def linha():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')


def contador(i,f,p):
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até o {f} de {p} em {p}',end=' ')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ', flush = True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush = True)
            sleep(0.5)
            cont -= p
        print('Fim')
    

linha()
contador(1,10,1)
contador(10,1,2)
print('Agora é a vez de personalizar a contagem:')
inicio = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Intervalo: '))
contador(inicio, fim,passo)


