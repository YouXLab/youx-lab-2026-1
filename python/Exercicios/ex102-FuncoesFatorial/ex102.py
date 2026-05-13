def fatorial(num, show=False):
    fatorial = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= cont
    return fatorial


print(fatorial(5, show=True))