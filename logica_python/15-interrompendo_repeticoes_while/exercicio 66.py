# Inicialização das variáveis
soma = 0
contador = 0

while True:
    # Lê o número do usuário
    n = int(input("Digite um número inteiro [999 para parar]: "))

    # Verifica a condição de parada (flag)
    if n == 999:
        break

    # Processa o número
    contador += 1
    soma += n

# Exibe os resultados finais
print(f"Foram digitados {contador} números.")
print(f"A soma entre eles (desconsiderando o 999) é {soma}.")
