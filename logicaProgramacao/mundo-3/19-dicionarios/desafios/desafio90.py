boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input('Media: '))
print(f'O nome é {boletim['nome']}')
print(f'A media é {boletim['media']}')
if boletim['media'] >= 7:
    print('Situação: Aprovado')
else:
    print('Siuação: Reprovado')