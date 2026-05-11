numero1=int(input('qual o numero? :'))
numero2=int(input('qual o numero? :'))
numero3=int(input('qual o numero? :'))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor= numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior= numero3
print(f'o menor numero é {menor} ')
print(f'o maior numero é {maior}')