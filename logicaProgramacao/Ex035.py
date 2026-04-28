Segmento = float(input('Digite o primeiro segmento: '))
Seg2 = float(input('Digite o segundo segmento: '))
Seg3 = float(input('Digite o terceiro segmento: '))
if (Segmento + Seg2 > Seg3) and (Segmento + Seg3 > Seg2) and (Seg3 + Seg2 > Segmento):
    print(f's segmentos {Segmento},{Seg2},e {Seg3} juntos podem formar um triangulo')
else:
    print('Os segmentos nao podem formar um triangulo')