nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = ( nota1 + nota2 ) / 2
print(f'tirando { nota1:.1f} e {nota2:.1f}, a media do aluno é {media:.1f}'.format(nota1, nota2, media))
if media >=5 and media < 7:
    print('o aluno esta em RECUPERACAO')
elif media >= 5:
    print('o aluno esta REPROVADO')
elif media >= 7:
    print('o aluno sera APROVADO')
    