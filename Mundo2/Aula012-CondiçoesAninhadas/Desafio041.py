#Classificando Atletas.
#A Confederaçao Nacional de Nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#-Ate 9 anos:MIRIM
#Ate 14 anos:INFANTIL
#Ate 19 anos:JUNIOR
#Ate 20 anos:SENIOR
#Acima:MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificaçao: MIRIM')
elif idade <= 14:
    print('Classificaçao: INFANTIL')
elif idade <= 19:
    print('Classificaçao: JUNIOR')
elif idade <=25:
    print('Classisficaçao: SENIOR')
else:
    print('Classificaçao: MASTER')