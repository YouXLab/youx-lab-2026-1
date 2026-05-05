somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1,5):
    print(f'Idade da pessoa {p}: ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print(f'A media da idade é {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomen} anos e se chama {nomevelho}')
print(f'E tem {totalmulher20} mulheres com menos de 20 anos')





