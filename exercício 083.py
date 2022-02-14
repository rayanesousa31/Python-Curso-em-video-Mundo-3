#Crie um programa onde o usuário digite um expressão qualquer que use
#parenteses. Seu aplicativo deverá analisar se a expressão passada está
#com os parenteses abertos e fechados na ordem correta.

expressão = str(input('Digite a função: '))
pilha = list()
for simbolo in expressão:
    if simbolo == '(':
       pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')        

