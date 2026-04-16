n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
s = n1 + n2
print('a soma vale',s)

#int= 7; -4; 0; 9875
#float= 4,5 ; 0.076; -15.223; 7.0
#bool= true; False
#str= 'Olá' ;'7.5' ;''

#forma diferente de usar o print
print('a soma vale', s)
print('a soma vale {}'.format(s))

#tipo do numero
n1 = int(input('digite um valor'))
print(type(n1))

#Mudando a resposta do print:
n1 = int(input('digite um valor'))
n2 = int(input('digite outro'))
s = n1+n2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
