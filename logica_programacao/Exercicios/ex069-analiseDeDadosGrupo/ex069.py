
sexo = ' '
idade= ' '
cont = 0
mulher= 0
homem = 0
while True:
    idade = int(input('digite sua idade'))
    sexo = str(input('informe seu sexo: [M/F]')).upper()
    if idade >= 18:
      cont += 1
    if sexo == 'M':
        homem+= 1
    if sexo == 'F' and idade <= 20:
     mulher += 1
    continuar = input('voce quer continuar [S/N]').upper()
    if continuar == 'N':
        break
print(f'{mulher} mulheres tem menos de 20 anos')
print(f'tem {cont} pessoas maior de 18 anos')
print(f'{homem} homens foram cadastrados')


