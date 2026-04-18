n = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    d = int(input("Digite um número de 0 a 20: "))
    if d <= 20:
        print("Você digitou o número {}".format(n[d]))
        break
    else:
        print("Número invalido! digite um número de 0 a 20")