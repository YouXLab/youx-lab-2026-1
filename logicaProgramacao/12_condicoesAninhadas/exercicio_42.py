reta1=float(input('primeiro segmento :'))
reta2=float(input('segundo segmento :'))
reta3=float(input('terceiro segmento :'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and  reta3 < reta1 + reta2:
    print('os segmentos acima podem formar um triangulo')
    if  reta1 == reta2 and reta2 == reta3:
        print('equilatero')
    elif reta1 != reta2 != reta3 != reta1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os segmentos a cima nao podem formar um triangulo')

