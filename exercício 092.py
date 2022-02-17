#Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente
#de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
#e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#35 anos de contribuição.
import datetime

info = dict()

info['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
info['ctps'] = int(input('Carteira de Trabalho (0 não possui):'))
info['idade'] = datetime.date.today().year - nasc
if info['ctps'] != 0:
   info['Contratação'] = int(input('Ano de contratação: '))
   info['Salário'] = float(input('Salário : R$'))   
   info['Aposentadoria'] = info['idade']+((info['Contratação'] + 35) - datetime.date.today().year)

print(info)
for a, b in info.items():
    print(f'- {a} tem valor:  {b}')






