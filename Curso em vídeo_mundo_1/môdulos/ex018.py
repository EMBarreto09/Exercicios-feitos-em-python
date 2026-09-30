#Calculo de um ângulo
import math

a = int(input('Digite o ângulo: '))

b = math.sin(a)
c = math.cos(a)
d = math.tan(a)

print(f'O seno de {a} é {b:.2f}\nO cosseno de {a} é {c:.2f}\nA tangente de {a} é {d:.2f}')