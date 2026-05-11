reta1=float(input('qual o comprimento da reta'))
reta2=float(input('qual o comprimento da reta'))
reta3=float(input('qual o comprimento da reta'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 + reta1 + reta3:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos nao podem formar triangulo')
