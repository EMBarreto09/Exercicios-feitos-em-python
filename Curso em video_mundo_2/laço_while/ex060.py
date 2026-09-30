#Fatorial
from math import factorial 

numero = int(input('Digite um número: '))
c = numero
print(f'Calculando {numero}!')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    c -= 1
    
print(factorial(numero))