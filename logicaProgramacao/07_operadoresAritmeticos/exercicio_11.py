rendimento = float(input('qual o rendimento da tinta por m2/l: '))
largura= float(input('digite o valor da largura'))
altura = float(input('altura da parede: '))
area = largura * altura
quantidadedetinta= (area / rendimento)
print (f'a quantidade de tintas é {quantidadedetinta}')