#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qul foi o maior e o menor valor digitado e suas 
#respectivas posições na lista.

valores = list()
menor = maior = 0
for v in range (0,5):
    valores.append(int(input(f'Digite um número para a posição {v} : ')))
    if v == 0 :
        maior = menor = valores[v]
    else:
        if valores [v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor foi {maior} na posição ',end=' ')
for i , v in enumerate(valores):
    if v == maior:
       print(f'{i}...',end=' ')
print(f'O menor valor foi {menor} na posição ',end =' ')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end=' ')



