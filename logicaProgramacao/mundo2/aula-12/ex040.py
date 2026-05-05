nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = nota1 + nota2 / 2
print('TIRANDO {:.1f} E {:.1f} A NOTA DO ALUNO E {:.1f}'.format(nota1,nota2,media))
if 7 > media >= 5:
    print('O ALUNO ESTA EM RECUPERACAO')
elif media < 5:
    print('O ALUNO ESTA REPROVADO')
elif media >= 7:
    print('O ALUNO ESTA APROVADO! PARABENS.')
    