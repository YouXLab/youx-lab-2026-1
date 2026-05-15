while True:
    numero= int(input('quer ver a tabuada de qual valor?'))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
