nome = str(input('Digite seu nome: ')).strip().upper()
if nome == 'ARTUR':
    print('Eita, nome mais lindo q ja vi em toda minha vida')
else:
    print('ah, nome meio sem graça, mas...')
print('Bom dia, {}!'.format(nome))

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média foi de {}, será que ta bom??'.format(media))
if media >= 6:
    print('CONGRATULATIONS!! you got approved!! (talentos bilíngues)')
else:
    print('Vish, sua média não foi suficiente, you got reproved! (talentos bilíngues)')
