base = int(input("digite um número: "));

print("-"*10, "A tabuada de", base, "é:", "-"*10);
for i in range(10):
#    print(i+1)
    print("{}x{} = {}".format(base, i+1, base * (i+1)));
print("-"*10)