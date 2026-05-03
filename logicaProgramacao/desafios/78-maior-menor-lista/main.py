ma = 0
me = 0
l = []
for i in range(0, 5):
    l.append(int(input(f"Digite o {i+1}° número: ")))
    if i == 0:
        ma = l[i]
        me = l[i]
    else:
        if l[i] > ma:
            ma = l[i]
        elif l[i] < me:
            me = l[i]
print("-"*20)
print(f"Você digitou os números: {l}")
print(f"Entre eles o maior foi {ma} nas posições: ", end="")
for i, e in enumerate(l):
    if e == ma:
        print(f"{i+1}, ", end="")
print(f"Entre eles o menor foi {me} nas posições ", end="")
for i, e in enumerate(l):
    if e == ma:
        print(f"{i+1}, ", end="")