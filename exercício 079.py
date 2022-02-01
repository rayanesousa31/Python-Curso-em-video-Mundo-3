#Crie um programa onde o usuário possa digitar vários valores numéricos e 
#cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
#será adicionado. No final, serão exibidos todos os valores únicos digitados,
#em ordem crescente.
opção = ' '
num = list()

while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não será adicionado...')
    opção = str(input('Que continuar?[S/N]').upper().strip() [0])
    if opção in 'Nn':
        break
num.sort()               
print(num)