import math
angulo = float(input("digite um angulo que deseja:"))
seno = math.sin(math.radians(angulo))
print("o angulo de {} tem o seno {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("o angulo de {} tem o cesseno de {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("o angulode {} tem o tangente de {:.2f}".format(angulo, tangente))
