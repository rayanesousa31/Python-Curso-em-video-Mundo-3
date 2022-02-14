#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
#em uma lista única que mantenha separadamente os valores pares e impares. No final,
#mostre os valores pares e impares em ordem crescente.


numeros = [[],[]]       #duas listas dentro de uma única lista
valor = 0
for n in range (1,8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
        numeros[0].sort()
    else:
        numeros[1].append(valor)
        numeros[1].sort()
print(numeros)
print(f'Os números pares são {numeros[0]}')
print(f'Os números impares são {numeros[1]}')



