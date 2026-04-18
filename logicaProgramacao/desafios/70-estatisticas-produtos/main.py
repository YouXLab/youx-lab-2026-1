print("-"*30)
print("    LOJA SUPER BARATÃO")
print("-"*30)
c = 0
t = 0
pm = 0
me = 0
nme = ""
while True:
    print("-"*20)
    c += 1
    print("REGISTRAR PRODUTO {}:".format(c))
    n = input("Nome: ")
    p = float(input("Preço: R$ "))
    if p < me:
        me = p
        nme = n
    if c == 1:
        me = p
        nme = n
    t += p
    if p > 1000:
        pm += 1
    o = input("Quer continuar? [S/N]: ")
    if o in "Nn":
        break
print("-"*20)
print("O total da compra foi R$ {}".format(t))
print("Temos no total {} produto custando mais de R$ 1000".format(pm))
print("O produto mais barato foi {} que custou: R$ {}".format(nme, me))