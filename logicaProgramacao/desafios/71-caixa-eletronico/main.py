print("---  BEM VINDO AO CAIXA ELETRONICO  ---")
s = int(input("Qual o valor que você deseja sacar?: R$ "))
t = s
n = 50
tn = 0
while True:
    if t >= n:
        t -= n
        tn += 1
    else:
        print("Total de {} notas de R$ {}".format(tn, n))
        if n == 50:
            n = 20
        elif n == 20:
            n = 10
        elif n == 10:
            n = 1
        tn = 0
        if t == 0:
            break
print("Atendimento encerrado, volte sempre!")