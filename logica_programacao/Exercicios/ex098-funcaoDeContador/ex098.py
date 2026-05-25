def contador(inicio, fim , passo):
    if passo == 0:
        passo = 1
    print('-='* 20)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        for c in range(inicio, fim - 1, -abs (passo)):
            print(c, end=' ')
    print('\n')
contador(10, 0, 2)
contador((1, 0, 2))
i=int(input('inicio: '))
f=int(input('fim: '))
p=int(input(('passo: ')))
contador(i,f,p)