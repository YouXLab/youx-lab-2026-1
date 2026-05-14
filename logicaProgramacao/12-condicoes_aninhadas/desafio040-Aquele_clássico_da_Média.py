primeiraNota =float(input('primeira nota: '))
segundaNota =float(input('segunda nota: '))
media = (primeiraNota + segundaNota) / 2
if media >= 5 and media < 7:
    print('você foi recuperação')
elif media <  5:
    print('você está de reprovado')
else:
    print('você foi aprovado')