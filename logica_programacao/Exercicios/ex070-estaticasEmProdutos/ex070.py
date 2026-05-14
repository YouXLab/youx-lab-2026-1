nome =' '
preco= 0
cont = ''
soma = 0
while True:
 nome=(input('qual é o nome do produto?'))
 preco=float(input('qual o valor do produto'))
 if preco > 1000:
     cont+= nome
 soma += preco
 barato = preco
 if preco < barato:
     barato = preco
 continuar = input('voce deseja continuar [S/N]').upper()
 if continuar == 'N':
   break
print(f'o produto mais barato foi{nome} que custa {barato}')
print(f'o total foi {soma}')
print(f'{cont} custaram mais de R$1000')



