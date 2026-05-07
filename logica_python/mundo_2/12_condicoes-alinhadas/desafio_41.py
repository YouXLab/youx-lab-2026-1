from datetime import date
atual = date.today().year
nascimento = (int(input('data de nascimento')))
idade = atual - nascimento
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificacao: MIRIM')
elif idade <= 14:
    print('classificacao: INFANTIL')
elif idade <= 19:
    print('classificacao: JUNIOR')
elif idade <=25:
    print('classificaco: SINIOR')
else:
    print('classificacao: MASTER')
    

