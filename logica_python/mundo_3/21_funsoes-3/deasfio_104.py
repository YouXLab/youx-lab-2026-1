def leiaInt(msg):
    n = input(msg)

    if n.isalnum():
        return int(n)
    else:
        print('ERRO!')
        return 0

    num = leiaInt('digite um numero: ')
    print(num)