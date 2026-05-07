primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = 3
for c in range(10):
    segundoTermo = primeiroTermo + razao
    primeiroTermo = segundoTermo
    print(segundoTermo)