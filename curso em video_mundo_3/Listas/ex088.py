#Mega sena
from random import randint
from time import sleep
lista = []
jogos = []
total = 1

escolha = int(input('Digite quantos jogos você quer: '))

while total <= escolha:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'{i+1}: {l}')
    sleep(1)

print('Fim')