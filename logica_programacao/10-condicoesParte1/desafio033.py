primeiroValor = float(input('Digite um valor:'))
segundoValor = float(input('Digite outro valor:'))
terceiroValor = float(input('Digite mais um valor:'))
lista = [primeiroValor, segundoValor, terceiroValor]
lista.sort() #.sort = organizar
print(f'O maior número é:', max(primeiroValor, segundoValor, terceiroValor))
print(f'O menor número é:', min(primeiroValor, segundoValor, terceiroValor))
