#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso mostre:
#-Quantos números foram digitados
#-A lista de valores ordenados de forma decrescente
#-Se o valor 5 foi digitado e está ou não na lista.
opção = ' '
lista = list ()
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Que continuar?[S/N]')).upper().strip() [0]
    if opção == 'N':
        break
if  5 in lista:
    print('O número 5 está na lista')
else:
    if 5 not in lista:
       print('O número 5 não foi digitado, por isso não esta na lista')
lista.sort(reverse = True)
print(lista)
print(f'Foram digitados {len(lista)} números')