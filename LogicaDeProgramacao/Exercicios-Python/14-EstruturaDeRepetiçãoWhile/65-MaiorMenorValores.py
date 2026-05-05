N2 = 0
N3 = 0
maior = 0
cont = 0
F1 = "Ss"
while F1 not in 'Nn':
    N1 = int(input('Digite um numero: '))
    F1 = str(input('Digite se quer continuar [Ss/Nn]: ').upper().strip())
    cont = cont + 1
    N2 = N2 + N1
    if N2 > maior:
        maior = N2
N3 = N2 / cont
print(f'Você digitou {cont} numeros e a media total deu {N3}')
print(f'O maior valor foi {maior}')