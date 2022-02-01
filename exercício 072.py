#Crie umm programa  que tenha uma tupla totalmente preenchida
#com a contagem por extensão, de zero até 20.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20)
#e mostrá-lo por extenso

número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete' , 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
print(número)
opção = 'S'
while True:
    cont = int(input('Digite um número de 0 a 20: '))
      
    if cont <= 20 and cont >=0  :
          break
    print('Tente novamente')
    
print(f'Você digitou o número {número[cont]}')


    
    

