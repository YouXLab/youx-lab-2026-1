numero1 = int(input('dgite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))
numero3 = int(input('digite o terceiro numero:'))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'o menor numero é {menor}')
print(f'o maior numero é maior {maior}')