#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
#composta.
from random import randint

lista = list()
jogos = list()
cont=0
total = 1
qnt = int(input('Quantos jogos você quer fazer? '))
while total <= qnt:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
           lista.append(num)
           cont +=1
        if cont >= 6:
           break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1
print()
for i, l in enumerate(jogos):
    print(f'O resultado do {i+1}º jogo é:{l} ')

