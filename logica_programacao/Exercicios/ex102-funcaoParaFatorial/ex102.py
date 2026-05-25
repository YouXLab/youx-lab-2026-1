def fatorial(num, show=False):
    dec = num
    count = 0
    result = 0
    fat = ''

    while count < num:
        count += 1
        fat += str(dec) + 'x'

        if count > 1:
            result = (result * dec)
        else:
            result = num

        dec -= 1

    if show:
        print(fat[:len(fat)-1], '=', '{}'.format(result))
    else:
        print(result)

fatorial(5, True)
help(fatorial)
