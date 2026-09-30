#Duas funções

from time import sleep
from random import randint

num = []

def sortear():
    for n in range(10):
        num.append(randint(1, 100))
    print(f'Valores sorteados...')
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.2)
def somar_par():
    par = 0
    for c in num:
        if c % 2 == 0:
            par += c
    print(f'\nA soma dos pares são {par}')

sortear()
somar_par()