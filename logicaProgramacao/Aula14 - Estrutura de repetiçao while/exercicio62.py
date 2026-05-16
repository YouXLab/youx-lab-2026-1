
print("Gerador de PA ")
num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
c = 1
n = 11
while c < n:
    print(num, end= ' > ')
    num += razao
    c += 1
    if c == n:
        s = int(input("Quantos termos a mais deseja ver? Digite 0 se quiser sair do programa "))
        n += s
        if s == 0:
            break