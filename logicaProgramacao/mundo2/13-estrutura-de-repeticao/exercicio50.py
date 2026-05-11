#Exercício Python 050: Desenvolva um programa que leia seis
# números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.
soma = 0
conta = 0
for c in range(1,7):
    numero =int(input(f'digite um {c} valor: '))
    soma += numero
    conta += 1
print(f'você irformou {soma} o numero e a soma foi {conta}')