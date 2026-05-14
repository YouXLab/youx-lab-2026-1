# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('🫶🏻'*30)
print('BRINCADEIRA DE CRIANÇA COM OPERAÇÕES COMPLEXAS?:')
print('🫶🏻'*30)
primeiroValor = int(input('QUAL SERÁ SEU PRIMEIRO VALOR?:'))
segundoValor = int(input('QUAL SERÁ SEU SEGUNDO VALOR?:'))
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
opcao = int(input('>>>>>>> QUAL É A SUA OPÇÃO?:'))
soma = primeiroValor + segundoValor
multiplicacao = primeiroValor * segundoValor
maior = [primeiroValor, segundoValor]
oMaior = max(maior)
print(soma)
print(multiplicacao)
print(oMaior)





