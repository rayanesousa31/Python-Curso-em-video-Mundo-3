#Crie um programa onde  o usuário possa digitar cinco valores numérico e 
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela

lista = list()

for l in range(0,5):
    valores = int(input('Digite um valor: '))
    if l == 0 or l > lista[-1]:
        lista.append(valores)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos< len(lista):
            if valores <= lista[pos]:
                lista.insert(pos,valores)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem são: {lista}')

