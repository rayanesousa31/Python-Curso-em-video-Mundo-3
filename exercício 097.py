#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
#como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    print('-'  * len(texto))
    print(texto)
    print('-' * len(texto))

escreva(' Rayane de Sousa ')
escreva(' Spyke ')
escreva(' Vitor de Brito Pereira ')

#------------RESOLUÇÃO GUSTAVO GUANABARA

def escreva(texto):
    tam = len(texto) + 4
    print('-'  * tam)
    print(f'  {texto}')
    print('-' * tam)

escreva(' Rayane de Sousa ')
escreva(' Spyke ')
escreva(' Vitor de Brito Pereira ')

    
       