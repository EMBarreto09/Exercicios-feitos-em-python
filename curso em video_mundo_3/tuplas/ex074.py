#Números na tupla

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))


#for numero in range(5):
#    menor = numero
#    maior = numero
#    for numero in numeros:
#        if numero > maior:
#            maior = numero
#        if numero < menor:
#            menor = numero

for numero in numeros:
    print(numero, end=' ')
    max 

print(f'Os números sortiados foram: {numeros}')
print(f'O maior valor dentre esses é o {max(numeros)}')
print(f'O menor valor dentre esses é o {min(numeros)}')

#print(f'Os números sortiados foram: {numeros}')
#print(f'O maior valor dentre esses é o {maior}')
#print(f'O menor valor dentre esses é o {menor}')
