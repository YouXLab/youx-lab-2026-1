soma= 0
media= 0
homem= 0
velho= ''
mulher= 0
for c in range(1, 5):
    nome= str(input('digte seu nome')). strip()
    idade= int(input('digte sua idade'))
    sexo= str(input('digte seu sexo')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        homem = idade
        velho = nome
    if sexo in 'Mm' and  idade > homem:
        homem = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
media= soma / 4
print(f'o homem mais velho tem {homem} anos e se chama {velho}')
print(f'tem {mulher} mulheres com menos de 20 anos ')
print(f'a idade media do grupo é {media}')

