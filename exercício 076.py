#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços na sequencia.
#No final, mostre uma listagem de preços, organizando os dados de forma tabular.

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 100.00,
            'Caneta', 22.30,
            'Livro', 34.90)

print('-' * 42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('-' * 42)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end= ' ')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
print('-' * 42)