def v(i):
    if i.isnumeric():
        return True
    else:
        return False
while True:
    numero = input("Digite o número: ")
    if v(numero):
        print(f"Você acabou de digitar o número {numero}")
    else: print("Erro! digite um número valido.")