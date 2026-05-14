print('-_=_-'*35)
print('Analisador de triângulos')
print('-_=_-'*35)
primeiraReta = float(input('Primeiro segmento:'))
segundaReta = float(input('Segundo segmento:'))
terceiraReta = float(input('Terceiro segmento:'))
if primeiraReta < segundaReta + terceiraReta and segundaReta < primeiraReta + terceiraReta and terceiraReta < segundaReta + primeiraReta:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo ;)')


