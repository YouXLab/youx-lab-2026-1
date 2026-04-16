p = int(input("Digite o primeiro segmento: "));
s = int(input("Digite o segundo segmento: "));
t = int(input("Digite o terceiro segmento: "));

if p == s and p == t:
    print("O triangulo é equilatero")
elif p == s or p == t or s == p or s == t or t == p or t == p:
    print("O triangulo é isósceles")
elif p != s and p != t and s != t and s != p and t != s and t != p:
    print("O triangulo é escaleno")