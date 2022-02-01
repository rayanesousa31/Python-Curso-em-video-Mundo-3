#Desenvolva um programa que leia quatro valores pelo teclado
#e guarde-os em uma tupla. No final mostre:
#-Quantas vezes apareceu o valor 9
#-Em que posição foi digitado o primeiro valor 3
#-Quais foram os números pares.
n = (int(input('Digite um número: ')), 
     int(input('Digite um número: ')), 
     int(input('Digite um número: ')), 
     int(input('Digite um número: ')))

print(f'{n}')

print(f'O número 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado')

for num in n:
    if num % 2 == 0:
        print(f'{num} é par')