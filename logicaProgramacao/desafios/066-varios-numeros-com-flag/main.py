num = soma = quant = 0
while num != 999:
    quant += 1
    num = int(input('Digite um número (999 para parar): '))
    if num != 999:
        soma += num
print(f'A soma dos {quant} números foi {soma} ')