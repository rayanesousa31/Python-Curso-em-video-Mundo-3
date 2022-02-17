#Faça um programa que tenha uma função chamada área(), que receba as imensões de um
#terreno retangular (largura e comprimento) e mostre a área do terreno.

def linha():
    print('-----------------------------')

def área(c,l):
    a = c*l
    if c != l :
       print(f'A área do terreno {l} por {c} é de {a}m^2')
    else:
        print('Esse terreno não é retangular')


print('CALCULANDO A ÁREA')
linha()
c = float(input(f'Comprimento (m): '))
l = float(input(f'Largura (m): '))
linha()
área(c,l)
