from datetime import date
atual= date.today().year
nascimento= int(input('qual a data de nascimento do atleta? :'))
idade= atual - nascimento
if idade <= 9:
    print('voce é mirim')
elif nascimento <= 14:
    print('voce é infantil')
elif idade <= 19:
    print('voce é junior')
elif idade <= 25:
    print('voce é senior')
else:
    print('voce é master')