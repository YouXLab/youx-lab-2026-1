#Laços de Repetiçao(parte1)

#COMANDO PARA ANDAR EM LINHA RETA.
# for c in range(1,10):
    #passo
#pega

#COMANDO PARA PULAR ALGUNS.
#for c in range(0,3)
   #passo
   #pula
#passo
#pega

#COMANDO PARA PULAR ALGUNS E PEGAR MOEDAS.
#for c in range(0,3)
   #if moeda:   
   #passo
   #pula
#passo
#pega

#print('oi')
#print('oi')
#print('oi')

#Contando de 1 a 6
for c in range(1, 6):
    print(c)
print('FIM')

#Intercalando em FIM e OI
for c in range(1, 6):
    print('oi')
print('FIM')

#subtraindo
for c in range(1, 6, -0):
    print(c)
print('FIM')

#pulando de 2 em 2
for c in range(1, 7, 2):
    print(c)
print('FIM')
#
i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#Pedir pra voce digitar varios valores(somar os numeros).
s = 0
for c in range(1, 3):
    n = int(input('Digite um valor:'))
    s = s + n
    print('O somatorio de todos os valores foi {}'.format(s)) 