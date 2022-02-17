#Faça um programa que tenha uma lista chamada números e duas
#funções chamadas sorteia() e somapar(). A primeira função vai
#sortear 5 números e vai colocá-los dentro da lista e a segunda 
#função vai mostrar a soma entre todos os valores pares sorteados
#pela função anterior.


from random import randint
números = []

def sorteia (lista):
    print('Sorteando 5 valores para a lista:')
    for cont in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n}', end= ' ')
print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+= valor
    print(f'A soma dos valores pares é {soma}')            

sorteia(números)
somapar(números)
