import math
a = float(input('Digite o valor do âgulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O seno, cosseno e tangente do ângulo {a} são respectivamente: {s:.2f}, {c:.2f}, {t:.2f}.')