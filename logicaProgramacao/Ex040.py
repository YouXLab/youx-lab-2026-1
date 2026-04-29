Nota1 = float(input('Primeira nota: '))
Nota2 = float(input('Segunda nota: '))
Media = (Nota1 + Nota2) / 2
print(f'Tirando {Nota1} e {Nota2} a media foi {Media}')
if Media <= 5:
    print('O ALUNO FOI REPROVADO!')
elif 5<Media<6.9:
    print('O ALUNO FICOU DE RECUPERACAO')
else:
    print('O ALUNO FOI APROVADO!')
