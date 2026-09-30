#Calculando a hipotenusa
from math import hypot, trunc

o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))

b = hypot(o, a)

print(f'O valor da hipotenusa é {b:.2f}')