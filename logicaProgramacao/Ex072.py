extensos = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze'
                ,'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito',
            "dezenove","vinte")
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('-=-' * 10)
    print('Tente novamente e', end= ' ')

print('-=-' * 10)
print(f'O usuario digitou o numero {extensos[numero]}')
print('-=-' * 10)

continuacao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
print('-=-' * 10)

while continuacao == 'S':
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('-=-' * 10)
    print('Tente novamente e', end=' ')

print('-=-' * 10)
print(f'O usuario digitou o numero {extensos[numero]}')

if continuacao == 'N':
    print('Programa Encerrado!')
