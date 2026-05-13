numero = ("zero", 'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
chance  = int(input('Digite um numero de 0 a 20: '))
while chance > 20:
    print('NUMERO INVALIDO. Tente novamente com um numero entre zero a vinte')
    chance = int(input('Digite um numero de 0 a 20: '))
print(numero[chance])