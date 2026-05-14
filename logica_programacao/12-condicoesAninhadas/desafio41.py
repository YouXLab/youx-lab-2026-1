from datetime import date
atual = date.today().year
print('---___===___---'*35)
print('Vamos analisar sua possível experiência como nadador...')
print('---___===___---'*35)
nascimento = int(input('Em que ano você nasceu?'))
idade = atual - nascimento
print(f"O atleta tem {idade} anos de idade,\nPortanto sua classificação como atleta é:")
if idade <= 9:
    print('Mirim...você é criança! ')
elif idade <= 14:
    print('Infantil...ainda é criança mas você cresceu!')
elif idade <= 19:
    print('Júnior...O JUNIN INCOSTA ZÉ!')
elif idade <= 25:
    print('Sênior...parece senhor?')
else:
    print('Master,Master!!!(Metallica: Master of Puppets = Referência!!!)')





