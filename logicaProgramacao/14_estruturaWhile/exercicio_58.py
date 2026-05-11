from random import randint
from random import randint
computador= randint(0, 5)
escolha= int(input('em que numero o computador pensou? (de 0 a 5 : ' ))
cont = 1
while computador != escolha:
    escolha = int(input('em que numero o computador pensou? (de 0 a 5 : '))
    cont += 1
print(f'voce acertou e usou {cont} palpites')