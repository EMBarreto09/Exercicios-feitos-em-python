#Porção inteira do número
from math import trunc

a = float(input('Digite um número decimal para achar a porção inteira: '))
b = trunc(a)
print(f'A porção inteira de {a} é {b}')
