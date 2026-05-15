somai=0
mediai=0
maiorI=0
mulher20= 0
nomev=' '
for p in range(1, 5):
    nome =input( 'digite seu nome:')
    idade=int(input('digite sua idade:'))
    sexo= input('digite seu sexo [M/F]:').upper()
    somai += idade
    if p == 1 and sexo =='M':
        maiorI = idade
        nomev = nome
    if sexo == 'M' and idade > maiorI:
        maiorI = idade
        nomev = nome
    if sexo =='F' and idade < 20:
        mulher20 += 1
        mediai= somai/4
        print(f" a media de idade do grupo é de {mediai} anos")
        print(f'o homem mais velho tem {maiorI} anos e se chama {nomev}')
        print(f'ao todo sao {mulher20} mulher com menos de 20 anos')
