print('='*80)
print('JOGO: OS 10 PRIMEIROS TERMOS DE UMA PA(PROGRESSÃO ARITMÉTICA):')
print('='*80)
primeiroTermo = int(input('Qual o 1° Termo?:'))
razao = int(input('Qual é a razão?:'))
for numeros in range(0, 10):
    progressaoAritmetica = primeiroTermo + (numeros - 1) * razao
    print(progressaoAritmetica+2)
print('FIM!!!')




