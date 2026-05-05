from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O ATLETA TEM {idade} anos')
if idade <= 9:
    print('A classificacao do atleta e: MIRIM')
elif idade <= 14:
    print ('A classificacao do atleta e: INFANTIL')
elif idade <= 19:
    print('A classificacao do atleta e: JUNIOR')
elif idade <= 25:
    print('A classificacao do atleta e: SENIOR')
else:
    print('A classificacao do atleta e: MASTER')

