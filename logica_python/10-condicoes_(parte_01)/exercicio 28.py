'''nome = str(input('Qual o seu nome? '))
if nome == 'Jennifer':
   print('Que nome lindo você tem!')
else:
   print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f"A sua média foi {m:.1f}")
if m >= 6.0:
   print('Sua média foi boa! PARABÉNS!')
else:
   print('Sua média foi ruim! ESTUDE MAIS!')'''


from random import randint
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}")













