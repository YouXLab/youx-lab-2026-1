from datetime import date
agora=date.today().year
nascimento= int(input('qual o ano de nascimento do jovem? :'))
idade= agora - nascimento
if idade == 18:
    print('voce deve se alistar imediatamente!')
elif idade < 18:
    tempo = 18 - idade
    print(f'voce ainda nao tem essa idade, falta {tempo} anos para se alistar')
elif idade > 18:
    tempo= idade - 18
    print(f'ja passou do prazo de se alistar, voce deveria se alistar em {tempo} anos')