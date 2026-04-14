import math
a = float(input("Digite o angulo que deseja: "));
se = math.sin(math.radians(a));
print("o angulo de {} tem o SENO de {:.2f}".format(a, se));
co = math.cos(math.radians(a));
print("o angulo de {} tem o COSSENO de {:.2f}".format(a, co));
ta = math.tan(math.radians(a));
print("o angulo de {} tem a TANGENTE de {:.2f}".format(a, ta));