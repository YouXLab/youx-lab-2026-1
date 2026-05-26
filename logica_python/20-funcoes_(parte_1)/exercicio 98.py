from time import sleep

def contador(inicio, fim, passo):
    # Ajusta o passo se for zero
    if passo == 0:
        passo = 1
    # Ajusta o passo se for negativo (trabalhamos com o valor absoluto para a lógica)
    if passo < 0:
        passo = abs(passo)

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")

    # Lógica para contagem crescente
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont += passo
        print("FIM!")
    # Lógica para contagem decrescente
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont -= passo
        print("FIM!")
    print("-" * 30)

# a) De 1 até 10, de 1 em 1
contador(1, 10, 1)

# b) De 10 até 0, de 2 em 2
contador(10, 0, 2)

# c) Contagem personalizada
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
f = int(input("Fim:    "))
pas = int(input("Passo:  "))

contador(ini, f, pas)
