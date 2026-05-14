from datetime import date
atual = date.today().year
nascimento =int(input('Que ano você nasceu: '))
idade = atual - nascimento
print(f'o atleta tem {idade} anos de idade')
if idade <= 9:
    print('classificação mirim')
elif idade <= 14:
    print('classificação infantil')
elif idade <= 19:
    print('classificação junior')
elif idade <= 25:
    print('classificação senior')
else:
    print('classificação master')