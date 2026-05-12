from datetime import datetime

def voto():
    ano = datetime.now().year
    idade = ano - nascimento
    if idade < 16:
        print(f'Voto com {idade} anos: negado')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'voto com {idade} anos: opcional')
    elif idade >= 18 and idade <= 65:
        print(f'Voto com {idade} anos: obrigatorio')

nascimento = int(input('Em que ano você nasceu? '))
voto()