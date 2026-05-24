
ficha = []
resposta = 's'
while resposta not in 'Nn':
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    resposta = input('Quer continuar? [S/N] ')
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
print(ficha)
