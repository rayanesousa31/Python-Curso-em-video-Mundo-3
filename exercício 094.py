#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os
#dicionários em uma lista. No final, mostre:
#- Quantas pessoas foram cadastradas
#- A média de idade do grupo
#- Uma lista com todas as mulheres
#- Uma lista com todas as pessoas com idade acima da média

pessoas = list()
pess = dict()
soma = media = 0
while True:
    pess.clear()
    pess['Nome'] = str(input('Nome: '))
    while True:
        pess['Sexo'] = str(input('Sexo [M/F] : ')).upper().strip()[0]
        if pess['Sexo'] in 'MmFf':
           break
        print('ERRO! Por favor, digite somente M ou F. ')
    pess['Idade'] = int(input('Idade: '))
    soma += pess['Idade']
    pessoas.append(pess.copy())
    while True:
        op = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
           break
        print('ERRO! Por favor, digite somente S ou N. ')
    if op == 'N':
        break    
print(pessoas)
print(f'1- Foram cadastradas {len(pessoas)} pessoas')
med = soma / len(pessoas)
print(f'2- A média de idade das pessoas cadastradas são :{med} anos')
print('3- A lista de mulheres cadastradas são:',end=' ')
for p in pessoas:
    if p['Sexo'] == 'F':
       print(p["Nome"])
print('4- As pessoas com idade acima da média: ')
for p in pessoas:
    if p['Idade'] >= med:
        print('   ',end='')
        for k, v in p.items():
            print(f' {k} = {v}',end='')
print('<<<ENCERRADO>>>')            



    
    