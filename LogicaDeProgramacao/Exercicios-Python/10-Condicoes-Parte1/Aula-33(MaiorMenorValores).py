N1 = int(input('Escreva o N1: '))
N2 = int(input('Escreva o N2: '))
N3 = int(input('Escreva o N3: '))

if N1 >= N2 and N1 >= N3:
    print(f'{N1} é o maior numero')
elif N2 >= N1 and N2 >=N3:
    print(f'{N2} é o maior numero')
elif N3 >= N1 and N3 >=N2:
    print(f'{N3} é o maior numero')

if N1 <= N2 and N1 <= N3:
    print(f'{N1} é o menor numero')
elif N2 <= N1 and N2 <=N3:
    print(f'{N2} é o menor numero')
elif N3 <= N1 and N3 <=N2:
    print(f'{N3} é o menor numero')

if N1 == N2 and N1 == N3:
    print(f'{N1} repetiu 3 vezes')
elif N2 == N1 and N2 == N3:
    print(f'{N2} repetiu 3 vezes')
elif N1 == N2 or N1 == N3:
    print(f'{N1} repetiu 2 vezes')
elif  N2 == N1 or N2 == N3:
    print(f'{N2} repetiu 2 vezes')

# maior = max(N1, N2, N3)
# menor = min(N1, N2, N3)
# print(maior)
# print(menor)