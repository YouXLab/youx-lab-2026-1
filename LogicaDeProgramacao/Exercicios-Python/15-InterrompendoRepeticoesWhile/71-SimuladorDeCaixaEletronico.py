



print('=========================================')
print('                Banco')
print('=========================================')
Din = int(input('      Quanto dinheiro quer sacar?'))

N100 = 0
N50 = 0
N20 = 0
N5 = 0
M1 = 0

while True:
    if Din >= 100:
        Din = Din - 100
        N100 = N100 + 1
    elif Din >= 50:
        Din = Din - 50
        N50 = N50 + 1
    elif Din >= 20:
        Din = Din - 20
        N20 = N20 + 1
    elif Din >= 5:
        Din = Din - 5
        N5 = N5 + 1
    elif Din >= 1:
        Din = Din - 1
        M1 = M1 + 1
    else:
        break
while True:
 if N100 == 1:
    print(f'Total de {N100} nota de R$100')
 elif N100 >= 2:
    print(f'Total de {N100} notas de R$100')
 if N50 == 1:
    print(f'Total de {N50} nota de R$50')
 elif N50 >= 2:
    print(f'Total de {N50} notas de R$50')
 if N20 == 1:
    print(f'Total de {N20} nota de R$20')
 elif N20 >= 2:
    print(f'Total de {N20} notas de R$20')
 if N5 == 1:
    print(f'Total de {N5} nota de R$5')
 elif N5 >= 2:
    print(f'Total de {N5} notas de R$5')
 if M1 == 1:
     print(f'Total de {M1} moeda de R$1')
 elif M1 >= 1:
     print(f'Total de {M1} moedas de R$1')
 if True:
     break
print('=========================================')






















