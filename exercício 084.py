#Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma 
#lista. No final mostre:
#- Quantas pessoas foram cadastradas.
#- Uma listagem com as pessoas mais pesadas
#- Uma listagem com as pessoas mais leves

total = list()
pessoas = list()
peso = list()
opção= ' '
cont= maior=menor=0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(total) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    total.append(pessoas[:])
    pessoas.clear()
    print(total)
    opção=' '
    cont+=1
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if opção == 'N':
        break
#print(f'Foram incluídos {cont} pessoas') #ou
print(f'Foram cadastrados {len(total)} pessoas')  
print(f'O maior peso é {maior}Kg',end = ' ')
for p in total:
    if p[1] == maior:
        print(f'{p[0]}',end= ' ')
print()        
print(f'O menor peso foi de {menor}Kg ',end = ' ')
for p in total:
    if p[1] == menor:
        print(f'{p[0]}',end= ' ')
print()        

