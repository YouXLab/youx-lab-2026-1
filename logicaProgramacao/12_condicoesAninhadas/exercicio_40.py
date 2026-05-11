nota1= int(input('digite a primeira nota'))
nota2= int(input('digite a segunda nota'))
media= (nota1 + nota2) / 2
print(f'tirando {nota1} e {nota2} a media vai ser {media}')
if media < 5 :
    print('voce esta reprovado!')
elif media == 5 or 6.9 :
    print('recuperacao')
elif media  >= 7:
    print('voce passou')