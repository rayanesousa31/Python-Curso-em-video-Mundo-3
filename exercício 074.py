#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também
#indique o menor número e o maior que estão em tupla.

from random import randint

n = (randint(0,10) , randint(0,10) , randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados são: ')
for num in n:
    print(f'{n}')
print(f'O maior número é: {max(n)}')  #max se usa em tuplas
print(f'O menor número é: {min(n)}')  #min se usa em tuplas
