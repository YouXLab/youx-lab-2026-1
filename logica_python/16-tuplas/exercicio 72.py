'''numero_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
    "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número: {numero_extenso[numero]}")
        break
    else:
        print("Tente novamente. ", end="")'''

salada = ('pepino', 'alface', 'couve', 'brocólis')
print(salada[1])
print(salada[-2])
print(salada[1:3])
print(salada[:2])
print(salada[1:3:])

numero_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
    "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(numero_extenso[18:2:-2])



