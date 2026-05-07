#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# -Media abaixo de 5.0: REPROVADO.
# -Media entre 5.0 e 6.9: RECUPERAÇAO.
# -Media 7.0 ou superior: APROVADO.

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if media >=5 and media < 7:
    print('O aluno esta em RECUPERAÇAO.')