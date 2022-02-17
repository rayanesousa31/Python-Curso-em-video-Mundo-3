#Crie um programa que leia nome e duas notas de vários alunos e 
# guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita 
# que o usuário possa mostrar as
#notas de cada aluno individualmente.

boletim = list()
nome = list()
nota = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    opção = ' '
    media = (nota + nota2) / 2
    boletim.append([nome, [nota, nota2],media])
    while opção not in 'SN':
        opção =  str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opção == 'N':
        break
print(boletim)
print('_' *30)
print(f'{"No.":<5}{"Nome":<10}{"Média":>8}')
print('_' * 30)
for i, a in enumerate(boletim):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8}')
while True:
    op = int (input('Digite o No do aluno que gostaria de consultar. (para finalizar digite 999 ) : '))
    if op == 999:
       break
    if op <= len(boletim) -1 : 
       print(f'Notas de {boletim[op][0]} sao {boletim[op][1]}')
    
  