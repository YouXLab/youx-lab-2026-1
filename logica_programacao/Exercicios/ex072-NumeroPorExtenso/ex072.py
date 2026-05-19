contagem=('zero', 'um' , 'dois' ,'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = float(input('digite um numero entre 0 e 20:'))
    if 0 <= numero <= 20:
        break
    else:
      print('tente novamente')


