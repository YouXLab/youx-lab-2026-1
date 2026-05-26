def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# 2. Chamando a função e passando os argumentos
valor = int(input('digite um valor: '))
valor2 = int(input('digite outro valor:'))
soma_final = somar(valor, valor2)
print(soma_final)